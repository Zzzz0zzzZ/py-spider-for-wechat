# coding=utf-8
# @Time : 2022/12/20 2:43 PM
# @Author : 王思哲
# @File : main.py
# @Software: PyCharm

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from getFakId import get_fakid
from getAllUrls import run_getAllUrls
from getContentsByUrls_MultiThread import run_getContentsByUrls_MultiThread


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(808, 687)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.user_info = QtWidgets.QGroupBox(self.centralwidget)
        self.user_info.setGeometry(QtCore.QRect(30, 70, 341, 191))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.user_info.setFont(font)
        self.user_info.setObjectName("user_info")
        self.token_label = QtWidgets.QLabel(self.user_info)
        self.token_label.setGeometry(QtCore.QRect(13, 43, 46, 18))
        self.token_label.setMinimumSize(QtCore.QSize(46, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.token_label.setFont(font)
        self.token_label.setObjectName("token_label")
        self.cookie_label = QtWidgets.QLabel(self.user_info)
        self.cookie_label.setGeometry(QtCore.QRect(13, 76, 46, 18))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cookie_label.sizePolicy().hasHeightForWidth())
        self.cookie_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cookie_label.setFont(font)
        self.cookie_label.setObjectName("cookie_label")
        self.token = QtWidgets.QLineEdit(self.user_info)
        self.token.setGeometry(QtCore.QRect(70, 42, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.token.setFont(font)
        self.token.setObjectName("token")
        self.cookie = QtWidgets.QTextEdit(self.user_info)
        self.cookie.setGeometry(QtCore.QRect(70, 80, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.cookie.setFont(font)
        self.cookie.setObjectName("cookie")
        self.clear_cookie_btn = QtWidgets.QPushButton(self.user_info)
        self.clear_cookie_btn.setGeometry(QtCore.QRect(134, 156, 101, 32))
        self.clear_cookie_btn.setObjectName("clear_cookie_btn")
        self.clear_all_btn = QtWidgets.QPushButton(self.user_info)
        self.clear_all_btn.setGeometry(QtCore.QRect(235, 156, 91, 32))
        self.clear_all_btn.setObjectName("clear_all_btn")
        self.wechat_pub_select = QtWidgets.QGroupBox(self.centralwidget)
        self.wechat_pub_select.setGeometry(QtCore.QRect(390, 70, 381, 191))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.wechat_pub_select.setFont(font)
        self.wechat_pub_select.setObjectName("wechat_pub_select")
        self.choose_wpub_res_label = QtWidgets.QLabel(self.wechat_pub_select)
        self.choose_wpub_res_label.setGeometry(QtCore.QRect(10, 110, 81, 21))
        self.choose_wpub_res_label.setMinimumSize(QtCore.QSize(46, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.choose_wpub_res_label.setFont(font)
        self.choose_wpub_res_label.setObjectName("choose_wpub_res_label")
        self.choose_wpub_res = QtWidgets.QComboBox(self.wechat_pub_select)
        self.choose_wpub_res.setGeometry(QtCore.QRect(100, 110, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.choose_wpub_res.setFont(font)
        self.choose_wpub_res.setObjectName("choose_wpub_res")
        self.wpub_name = QtWidgets.QLineEdit(self.wechat_pub_select)
        self.wpub_name.setGeometry(QtCore.QRect(100, 50, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.wpub_name.setFont(font)
        self.wpub_name.setObjectName("wpub_name")
        self.wpub_search = QtWidgets.QPushButton(self.wechat_pub_select)
        self.wpub_search.setGeometry(QtCore.QRect(290, 47, 81, 41))
        self.wpub_search.setObjectName("wpub_search")
        self.layoutWidget = QtWidgets.QWidget(self.wechat_pub_select)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 45, 77, 46))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.wpub_name_label = QtWidgets.QLabel(self.layoutWidget)
        self.wpub_name_label.setMinimumSize(QtCore.QSize(46, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.wpub_name_label.setFont(font)
        self.wpub_name_label.setObjectName("wpub_name_label")
        self.verticalLayout_3.addWidget(self.wpub_name_label)
        self.wpub_notice_label = QtWidgets.QLabel(self.layoutWidget)
        self.wpub_notice_label.setMinimumSize(QtCore.QSize(46, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.wpub_notice_label.setFont(font)
        self.wpub_notice_label.setObjectName("wpub_notice_label")
        self.verticalLayout_3.addWidget(self.wpub_notice_label)
        self.crab_settings = QtWidgets.QGroupBox(self.centralwidget)
        self.crab_settings.setGeometry(QtCore.QRect(30, 270, 741, 131))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.crab_settings.setFont(font)
        self.crab_settings.setObjectName("crab_settings")
        self.start_page_label = QtWidgets.QLabel(self.crab_settings)
        self.start_page_label.setGeometry(QtCore.QRect(10, 45, 71, 21))
        self.start_page_label.setMinimumSize(QtCore.QSize(46, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.start_page_label.setFont(font)
        self.start_page_label.setObjectName("start_page_label")
        self.start_page = QtWidgets.QSpinBox(self.crab_settings)
        self.start_page.setGeometry(QtCore.QRect(80, 45, 48, 24))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.start_page.setFont(font)
        self.start_page.setObjectName("start_page")
        self.crab_page_label = QtWidgets.QLabel(self.crab_settings)
        self.crab_page_label.setGeometry(QtCore.QRect(10, 85, 71, 21))
        self.crab_page_label.setMinimumSize(QtCore.QSize(46, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.crab_page_label.setFont(font)
        self.crab_page_label.setObjectName("crab_page_label")
        self.crab_page = QtWidgets.QSpinBox(self.crab_settings)
        self.crab_page.setGeometry(QtCore.QRect(80, 85, 48, 24))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.crab_page.setFont(font)
        self.crab_page.setObjectName("crab_page")
        self.save_filepath = QtWidgets.QTextBrowser(self.crab_settings)
        self.save_filepath.setGeometry(QtCore.QRect(260, 85, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.save_filepath.setFont(font)
        self.save_filepath.setObjectName("save_filepath")
        self.choose_path_btn = QtWidgets.QPushButton(self.crab_settings)
        self.choose_path_btn.setGeometry(QtCore.QRect(496, 80, 91, 32))
        self.choose_path_btn.setObjectName("choose_path_btn")
        self.save_filepath_label = QtWidgets.QLabel(self.crab_settings)
        self.save_filepath_label.setGeometry(QtCore.QRect(170, 85, 81, 21))
        self.save_filepath_label.setMinimumSize(QtCore.QSize(46, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.save_filepath_label.setFont(font)
        self.save_filepath_label.setObjectName("save_filepath_label")
        self.save_filename = QtWidgets.QLineEdit(self.crab_settings)
        self.save_filename.setGeometry(QtCore.QRect(260, 46, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.save_filename.setFont(font)
        self.save_filename.setObjectName("save_filename")
        self.start_btn = QtWidgets.QPushButton(self.crab_settings)
        self.start_btn.setGeometry(QtCore.QRect(599, 36, 131, 91))
        self.start_btn.setObjectName("start_btn")
        self.save_filename_label = QtWidgets.QLabel(self.crab_settings)
        self.save_filename_label.setGeometry(QtCore.QRect(170, 46, 81, 21))
        self.save_filename_label.setMinimumSize(QtCore.QSize(46, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.save_filename_label.setFont(font)
        self.save_filename_label.setObjectName("save_filename_label")
        self.crab_progress = QtWidgets.QGroupBox(self.centralwidget)
        self.crab_progress.setGeometry(QtCore.QRect(30, 410, 741, 211))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.crab_progress.setFont(font)
        self.crab_progress.setObjectName("crab_progress")
        self.progress_bar = QtWidgets.QProgressBar(self.crab_progress)
        self.progress_bar.setGeometry(QtCore.QRect(80, 50, 601, 21))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.progress_bar.setFont(font)
        self.progress_bar.setProperty("value", 24)
        self.progress_bar.setObjectName("progress_bar")
        self.progress_bar_label = QtWidgets.QLabel(self.crab_progress)
        self.progress_bar_label.setGeometry(QtCore.QRect(10, 50, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.progress_bar_label.setFont(font)
        self.progress_bar_label.setObjectName("progress_bar_label")
        self.info_label = QtWidgets.QLabel(self.crab_progress)
        self.info_label.setGeometry(QtCore.QRect(9, 80, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.info_label.setFont(font)
        self.info_label.setObjectName("info_label")
        self.log_info = QtWidgets.QTextBrowser(self.crab_progress)
        self.log_info.setGeometry(QtCore.QRect(80, 80, 641, 111))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.log_info.setFont(font)
        self.log_info.setObjectName("log_info")
        self.progress_bar_percentage = QtWidgets.QLabel(self.crab_progress)
        self.progress_bar_percentage.setGeometry(QtCore.QRect(690, 50, 31, 16))
        self.progress_bar_percentage.setObjectName("progress_bar_percentage")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(300, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setUnderline(True)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.app_version = QtWidgets.QLabel(self.centralwidget)
        self.app_version.setGeometry(QtCore.QRect(460, 22, 60, 16))
        self.app_version.setObjectName("app_version")
        self.contact_author = QtWidgets.QLabel(self.centralwidget)
        self.contact_author.setGeometry(QtCore.QRect(561, 40, 211, 16))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.contact_author.setFont(font)
        self.contact_author.setObjectName("contact_author")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 22))
        self.menubar.setWhatsThis("")
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.toolBar.setFont(font)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionbangzhu = QtWidgets.QAction(MainWindow)
        self.actionbangzhu.setObjectName("actionbangzhu")
        self.actiontuichu = QtWidgets.QAction(MainWindow)
        self.actiontuichu.setObjectName("actiontuichu")
        self.menu.addAction(self.actionbangzhu)
        self.menu.addSeparator()
        self.menu.addAction(self.actiontuichu)
        self.menubar.addAction(self.menu.menuAction())
        self.toolBar.addAction(self.actionbangzhu)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actiontuichu)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "微信公众号爬虫v1.0.0"))
        self.user_info.setTitle(_translate("MainWindow", "用户登陆"))
        self.token_label.setText(_translate("MainWindow", "token"))
        self.cookie_label.setText(_translate("MainWindow", "cookie"))
        self.clear_cookie_btn.setText(_translate("MainWindow", "清空cookie"))
        self.clear_all_btn.setText(_translate("MainWindow", "全部清空"))
        self.wechat_pub_select.setTitle(_translate("MainWindow", "公众号选择"))
        self.choose_wpub_res_label.setText(_translate("MainWindow", "选择公众号"))
        self.wpub_search.setText(_translate("MainWindow", "查询"))
        self.wpub_name_label.setText(_translate("MainWindow", "公众号名称"))
        self.wpub_notice_label.setText(_translate("MainWindow", "(支持模糊查询)"))
        self.crab_settings.setTitle(_translate("MainWindow", "爬取设置"))
        self.start_page_label.setText(_translate("MainWindow", "起始页码"))
        self.crab_page_label.setText(_translate("MainWindow", "爬取页数"))
        self.choose_path_btn.setText(_translate("MainWindow", "选择..."))
        self.save_filepath_label.setText(_translate("MainWindow", "保存位置"))
        self.start_btn.setText(_translate("MainWindow", "开始爬取"))
        self.save_filename_label.setText(_translate("MainWindow", "保存文件名"))
        self.crab_progress.setTitle(_translate("MainWindow", "爬取进度"))
        self.progress_bar_label.setText(_translate("MainWindow", "进度条"))
        self.info_label.setText(_translate("MainWindow", "日志信息"))
        self.progress_bar_percentage.setText(_translate("MainWindow", "25%"))
        self.title.setText(_translate("MainWindow", "微信公众号爬虫"))
        self.app_version.setText(_translate("MainWindow", "v1.0.0"))
        self.contact_author.setText(_translate("MainWindow", "联系作者：wsz2002@foxmail.com"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionbangzhu.setText(_translate("MainWindow", "帮助"))
        self.actiontuichu.setText(_translate("MainWindow", "退出"))
        self.choose_wpub_res.addItem('请在查询后选择您要爬取的公众号')

    def bind_funcs(self):
        # 绑定选择路径
        self.choose_path_btn.clicked.connect(lambda: self.slot_choose_savepath(self.choose_path_btn))
        # 绑定开始按钮
        self.start_btn.clicked.connect(self.start_crab)
        # 清空cookie 和 全部清空
        self.clear_cookie_btn.clicked.connect(self.slot_clear_cookie)
        self.clear_all_btn.clicked.connect(self.slot_clear_all)
        # 绑定公众号名称搜索
        self.wpub_search.clicked.connect(self.slot_wpub_search)

    def slot_wpub_search(self):
        # 获取token
        self.tok_str = self.token.text()
        # 获取cookie
        self.cok_str = self.cookie.toPlainText()
        print("cookie", self.cok_str, type(self.cok_str))
        # 请求头
        self.headers = {
            "cookie": self.cok_str,
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
        }
        # 要查询的公众号名
        self.wpub_name_str = self.wpub_name.text()
        print('wpub_name', self.wpub_name_str, type(self.wpub_name_str))
        # 查询公众号及fakid
        self.wpub_search_res = get_fakid(self.headers, self.tok_str, self.wpub_name_str)
        print(self.wpub_search_res)
        # 添加到comboBox(先清空默认提示, 后添加)
        self.choose_wpub_res.clear()
        self.choose_wpub_res.addItems([f"{x['wpub_name']}   {x['wpub_fakid']}" for x in self.wpub_search_res])

    def slot_clear_cookie(self):
        self.cookie.clear()

    def slot_clear_all(self):
        self.cookie.clear()
        self.token.clear()

    def slot_choose_savepath(self, button):
        self.selected_path_str = QFileDialog.getExistingDirectory(None, "选取文件夹", "./")
        if self.selected_path_str != '':
            self.save_filepath.setText(self.selected_path_str)
        button.toggle()

    def start_crab(self):
        # 起始页, 页数, 保存路径(最后无'/'), 文件名(会自动添加.csv后缀)
        self.start_page_int = int(self.start_page.text())
        self.crab_page_int = int(self.crab_page.text())
        self.save_filepath_str = self.save_filepath.toPlainText()
        self.save_filename_str = self.save_filename.text()

        # 当前选择的公众号的下标
        wpub_selected_index = self.choose_wpub_res.currentIndex()
        # 当前选择的公众号的fakeid
        wpub_selected_fakid = self.wpub_search_res[wpub_selected_index]['wpub_fakid']

        # 获取所有文章url
        run_getAllUrls(
            page_start=self.start_page_int,
            page_num=self.crab_page_int,
            save_path=self.save_filepath_str,
            tok=self.tok_str,
            fad=wpub_selected_fakid,
            headers=self.headers,
            filename=self.save_filename_str
        )

        # 多线程根据url获取content
        run_getContentsByUrls_MultiThread(
            savepath=self.save_filepath_str,
            filename=self.save_filename_str,
            headers=self.headers
        )

        # 已选择公众号下标
        print('[][][][][][]', wpub_selected_index, type(wpub_selected_index))

        ##### 正则!!! #####


if __name__ == "__main__":
    # 实例化app对象
    app = QApplication(sys.argv)
    # 实例化主窗口对象
    mainWindow = QMainWindow()
    # 实例化ui类
    ui = Ui_MainWindow()
    # 调用类内方法setupUi(), 传入窗口对象
    ui.setupUi(mainWindow)
    ui.bind_funcs()
    # 显示窗口
    mainWindow.show()
    # 进入主循环，通过exit确保主循环安全结束
    sys.exit(app.exec_())