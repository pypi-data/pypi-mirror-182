from .devoud_data import *
from .pages import PagesObserver, embedded_pages
from .browser_embedded_view import EmbeddedPage
from .browser_web_view import BrowserWebView
import re

url_protocol_pattern = re.compile(r'^(?:http|https|ftp|ftps|devoud|file)://', re.IGNORECASE)
url_pattern = re.compile("^[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$")


class BrowserPageWrapper(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.tab_widget = parent
        self.window = parent.window()
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setObjectName("progress_bar")
        self.progress_bar.setFixedHeight(4)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(False)
        self.layout.addWidget(self.progress_bar)

        self.url = 'devoud://void'
        self.view = None
        self.create_embedded_view(self.url)
        self.title = self.view.title

    def create_web_view(self):
        self.view = BrowserWebView(self)
        self.view.titleChanged.connect(lambda new_title: self.update_title(new_title))
        self.view.page().urlChanged.connect(self.url_changed)
        self.view.loadStarted.connect(self.loadStartedHandler)
        self.view.loadProgress.connect(self.loadProgressHandler)
        self.view.loadFinished.connect(self.loadFinishedHandler)
        self.layout.addWidget(self.view)

    def create_embedded_view(self, url='devoud://void'):
        try:
            self.view = embedded_pages[url](self)
        except KeyError:
            self.load('devoud://notfound')
        self.layout.addWidget(self.view)

    @staticmethod
    def is_url(url):
        """По протоколу либо по домену"""
        return (re.match(url_protocol_pattern, url) is not None) or (re.match(url_pattern, url) is not None)

    @staticmethod
    def return_type_by_ulr(url):
        return EmbeddedPage if url[:9].lower() == 'devoud://' else BrowserWebView

    def load(self, url: str, allow_search=False):
        if url == 'about:blank':
            url = 'devoud://notfound'
        formatted_url = QUrl.fromUserInput(url).toString()
        if not isinstance(self.view, BrowserPageWrapper.return_type_by_ulr(url)):
            self._convert_page_type()
            self.load(url)
        else:
            if self.view.embedded:
                self.view.deleteLater()
                self.create_embedded_view(url)
            else:
                # для веб-страницы
                if self.is_url(url):
                    # если это ссылка, то блокируем поиск
                    allow_search = False
                if allow_search:
                    # при разрешении вставляем текст в поисковый движок
                    self.view.load(f'{search_engines[self.window.search_box.currentText()][0]}{url}')
                else:
                    self.view.load(formatted_url)

        self.url = url
        PagesObserver.control_update_lists()
        self.update_title(self.view.title)

    def reload(self):
        self.view.reload()

    def back(self):
        self.view.back()

    def forward(self):
        self.view.forward()

    def _convert_page_type(self):
        self.view.deleteLater()
        if self.view.embedded:
            self.create_web_view()
        else:
            self.create_embedded_view()

    def url_changed(self, url):
        if isinstance(url, QUrl):
            self.url = url.toString()
        if FS.get_option('saveHistory'):
            with open(f'{FS.config_dir()}/history', 'a') as history_file:
                history_file.write(self.url + '\n')
        if self.tab_widget.currentWidget() == self:
            self.window.address_edit.setText(self.url)
            self.window.address_edit.setCursorPosition(0)
            self.window.check_state_bookmark()
        PagesObserver.control_update_lists()

    def update_title(self, title):
        self.title = title
        index = self.tab_widget.indexOf(self)
        self.tab_widget.setTabText(index, title)
        if self.tab_widget.currentWidget() == self:
            self.window.set_title(title)

    @QtCore.Slot()
    def loadStartedHandler(self):
        print(f"[Загрузка]: Начата загрузка страницы ({self.url})")

    @QtCore.Slot(int)
    def loadProgressHandler(self, progress):
        self.progress_bar.setValue(progress)
        print(f"[Загрузка]: {progress}% ({self.url})")

    @QtCore.Slot()
    def loadFinishedHandler(self):
        self.progress_bar.setValue(0)
        print(f"[Загрузка]: Страница загружена ({self.url})")

