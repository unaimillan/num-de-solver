from ui.markup_old import MyFrame1

import wx

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame1(None)
    frame.Show()
    app.MainLoop()
