import math
import matplotlib
import wx
import wx.xrc
from matplotlib.figure import Figure
import numpy as np

from solvers.exact import Exact
from solvers.euler import Euler
from solvers.improved_euler import ImprovedEuler
from solvers.runge_kutta import RungeKutta

matplotlib.use('wxagg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg


class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"D.E. Assignment",
                          pos=wx.DefaultPosition, size=wx.Size(1135, 717),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        fgSizer3 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer3.AddGrowableCol(1)
        fgSizer3.AddGrowableRow(0)
        fgSizer3.SetFlexibleDirection(wx.BOTH)
        fgSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        fgSizer4 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer4.SetFlexibleDirection(wx.BOTH)
        fgSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"x0",
                                           wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText1.Wrap(-1)

        fgSizer4.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL,
                     5)

        self.m_spinCtrlDouble1 = wx.SpinCtrlDouble(self, wx.ID_ANY,
                                                   wx.EmptyString,
                                                   wx.DefaultPosition,
                                                   wx.DefaultSize,
                                                   wx.SP_ARROW_KEYS, -100, 100,
                                                   0, 0.1)
        self.m_spinCtrlDouble1.SetDigits(3)
        fgSizer4.Add(self.m_spinCtrlDouble1, 0, wx.ALL, 5)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"y0",
                                           wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText2.Wrap(-1)

        fgSizer4.Add(self.m_staticText2, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL,
                     5)

        self.m_spinCtrlDouble11 = wx.SpinCtrlDouble(self, wx.ID_ANY,
                                                    wx.EmptyString,
                                                    wx.DefaultPosition,
                                                    wx.DefaultSize,
                                                    wx.SP_ARROW_KEYS, -100, 100,
                                                    math.sqrt(1 / 2), 0.1)
        self.m_spinCtrlDouble11.SetDigits(3)
        fgSizer4.Add(self.m_spinCtrlDouble11, 0, wx.ALL, 5)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"X",
                                           wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText3.Wrap(-1)

        fgSizer4.Add(self.m_staticText3, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL,
                     5)

        self.m_spinCtrlDouble12 = wx.SpinCtrlDouble(self, wx.ID_ANY,
                                                    wx.EmptyString,
                                                    wx.DefaultPosition,
                                                    wx.DefaultSize,
                                                    wx.SP_ARROW_KEYS, -100, 100,
                                                    3, 0.1)
        self.m_spinCtrlDouble12.SetDigits(3)
        fgSizer4.Add(self.m_spinCtrlDouble12, 0, wx.ALL, 5)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"N",
                                           wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText7.Wrap(-1)

        fgSizer4.Add(self.m_staticText7, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL,
                     5)

        self.m_spinCtrl1 = wx.SpinCtrl(self, wx.ID_ANY, wx.EmptyString,
                                       wx.DefaultPosition, wx.DefaultSize,
                                       wx.SP_ARROW_KEYS, 1, 10000, 15)
        fgSizer4.Add(self.m_spinCtrl1, 0, wx.ALL, 5)

        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, u"N_i",
                                           wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText8.Wrap(-1)

        fgSizer4.Add(self.m_staticText8, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL,
                     5)

        self.m_spinCtrl11 = wx.SpinCtrl(self, wx.ID_ANY, wx.EmptyString,
                                        wx.DefaultPosition, wx.DefaultSize,
                                        wx.SP_ARROW_KEYS, 1, 10000, 10)
        fgSizer4.Add(self.m_spinCtrl11, 0, wx.ALL, 5)

        self.m_staticText9 = wx.StaticText(self, wx.ID_ANY, u"N_f",
                                           wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText9.Wrap(-1)

        fgSizer4.Add(self.m_staticText9, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL,
                     5)

        self.m_spinCtrl12 = wx.SpinCtrl(self, wx.ID_ANY, wx.EmptyString,
                                        wx.DefaultPosition, wx.DefaultSize,
                                        wx.SP_ARROW_KEYS, 1, 10000, 50)
        fgSizer4.Add(self.m_spinCtrl12, 0, wx.ALL, 5)

        bSizer3.Add(fgSizer4, 0, wx.EXPAND | wx.ALL, 5)

        self.m_staticText10 = wx.StaticText(self, wx.ID_ANY, u"Soutions:",
                                            wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText10.Wrap(-1)

        bSizer3.Add(self.m_staticText10, 0, wx.ALL, 5)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_checkBox5 = wx.CheckBox(self, wx.ID_ANY, u"Exact",
                                       wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_checkBox5.SetValue(True)
        bSizer6.Add(self.m_checkBox5, 0, wx.ALL, 5)

        self.m_checkBox6 = wx.CheckBox(self, wx.ID_ANY, u"Euler",
                                       wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_checkBox6.SetValue(True)
        bSizer6.Add(self.m_checkBox6, 0, wx.ALL, 5)

        self.m_checkBox7 = wx.CheckBox(self, wx.ID_ANY, u"Improved Euler",
                                       wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_checkBox7.SetValue(True)
        bSizer6.Add(self.m_checkBox7, 0, wx.ALL, 5)

        self.m_checkBox8 = wx.CheckBox(self, wx.ID_ANY, u"Runge-Kutta",
                                       wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_checkBox8.SetValue(True)
        bSizer6.Add(self.m_checkBox8, 0, wx.ALL, 5)

        bSizer3.Add(bSizer6, 0, wx.EXPAND | wx.TOP | wx.BOTTOM | wx.LEFT, 5)

        self.button_calc = wx.Button(self, wx.ID_ANY, u"Calculate",
                                     wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.button_calc, 0, wx.ALL, 5)

        fgSizer3.Add(bSizer3, 1, wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        # self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.figure4 = MyMatplotFigure()
        # self.subplot41 = self.figure4.add_subplot(3, 1, 2)
        # self.subplot41 = self.figure4.add_subplot(3, 1, 3)
        # self.subplot4.plot([0, 1, 2], [0, 10, 0])
        self.m_panel4 = FigureCanvasWxAgg(self, wx.ID_ANY, self.figure4)
        bSizer4.Add(self.m_panel4, 1, wx.EXPAND | wx.ALL, 5)
        self.update_all_plots()

        """self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        figure = Figure()
        subplot = figure.add_subplot()
        subplot.plot([0,1,2], [20,10,20])
        self.m_panel5 = FigureCanvasWxAgg(self, wx.ID_ANY, figure)
        bSizer4.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )
"""

        fgSizer3.Add(bSizer4, 1, wx.EXPAND, 5)

        self.SetSizer(fgSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_spinCtrlDouble1.Bind(wx.EVT_SPINCTRLDOUBLE,
                                    self.m_spinCtrlDouble1OnSpinCtrlDouble)
        self.m_spinCtrlDouble11.Bind(wx.EVT_SPINCTRLDOUBLE,
                                     self.m_spinCtrlDouble1OnSpinCtrlDouble)
        self.m_spinCtrlDouble12.Bind(wx.EVT_SPINCTRLDOUBLE,
                                     self.m_spinCtrlDouble1OnSpinCtrlDouble)
        self.m_spinCtrl1.Bind(wx.EVT_SPINCTRL, self.m_spinCtrl1OnSpinCtrl)
        self.m_spinCtrl11.Bind(wx.EVT_SPINCTRL, self.m_spinCtrl1OnSpinCtrl)
        self.m_spinCtrl12.Bind(wx.EVT_SPINCTRL, self.m_spinCtrl1OnSpinCtrl)
        self.m_checkBox5.Bind(wx.EVT_CHECKBOX, self.m_checkBox5OnCheckBox)
        self.m_checkBox6.Bind(wx.EVT_CHECKBOX, self.m_checkBox5OnCheckBox)
        self.m_checkBox7.Bind(wx.EVT_CHECKBOX, self.m_checkBox5OnCheckBox)
        self.m_checkBox8.Bind(wx.EVT_CHECKBOX, self.m_checkBox5OnCheckBox)
        self.button_calc.Bind(wx.EVT_BUTTON, self.button_calcOnButtonClick)
        self.Bind(wx.EVT_CHAR_HOOK, self.close_window)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def close_window(self, event):
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            self.Close()
        else:
            event.Skip()

    def m_spinCtrlDouble1OnSpinCtrlDouble(self, event):
        self.button_calcOnButtonClick(event)

    def m_spinCtrl1OnSpinCtrl(self, event):
        self.button_calcOnButtonClick(event)

    def m_checkBox5OnCheckBox(self, event):
        self.button_calcOnButtonClick(event)

    def button_calcOnButtonClick(self, event: wx.Event):
        self.update_all_plots()

    def update_all_plots(self):
        print("Buttons:", self.m_checkBox5.IsChecked(),
              self.m_checkBox6.IsChecked(), self.m_checkBox7.IsChecked(),
              self.m_checkBox8.IsChecked())
        print("Starting!")

        self.figure4.x0 = float(self.m_spinCtrlDouble1.GetValue())
        self.figure4.y0 = float(self.m_spinCtrlDouble11.GetValue())
        self.figure4.X = float(self.m_spinCtrlDouble12.GetValue())
        self.figure4.n = int(self.m_spinCtrl1.GetValue())
        self.figure4.n_i = int(self.m_spinCtrl11.GetValue())
        self.figure4.n_f = int(self.m_spinCtrl12.GetValue())
        self.figure4.isExact = bool(self.m_checkBox5.IsChecked())
        self.figure4.isEuler = bool(self.m_checkBox6.IsChecked())
        self.figure4.isImprovedEuler = bool(self.m_checkBox7.IsChecked())
        self.figure4.isRungeKutta = bool(self.m_checkBox8.IsChecked())

        self.figure4.refresh()
        self.m_panel4.draw()
        print("Drawn!", len(self.m_panel4.figure.axes),
              len(self.figure4.axes1.lines))


class MyMatplotFigure(Figure):
    def __init__(self):
        super().__init__()
        self.y0 = math.sqrt(1 / 2)
        self.x0 = 0
        self.X = 3
        self.n = 15
        self.n_i = 10
        self.n_f = 20
        self.isExact = True
        self.isEuler = True
        self.isImprovedEuler = True
        self.isRungeKutta = True
        self.axes1 = self.add_subplot(311, title='Solution')
        self.axes2 = self.add_subplot(312,
                                      title='Local approximation error')
        self.axes3 = self.add_subplot(313,
                                      title='Total approximation error')
        self.set_tight_layout("True")

    def refresh(self):
        x0 = self.x0
        y0 = self.y0
        X = self.X
        n = self.n
        # X = 3
        # y0 = math.sqrt(0.5)
        ex = Exact(x0, y0, X)
        eu = Euler(x0, y0, X)
        ieu = ImprovedEuler(x0, y0, X)
        rk = RungeKutta(x0, y0, X)

        self.axes1.clear()
        self.axes1.set_title('Solution')
        # n = 25
        x = ex.x_list(n)
        y1 = ex.solve(n)
        y2 = eu.solve(n)
        y3 = ieu.solve(n)
        y4 = rk.solve(n)
        if self.isExact:
            self.axes1.plot(x, y1, label="Exact", color='#1f77b4')
        if self.isEuler:
            self.axes1.plot(x, y2, label="Euler", color='#ff7f0e')
        if self.isImprovedEuler:
            self.axes1.plot(x, y3, label="Improved Euler", color='#2ca02c')
        if self.isRungeKutta:
            self.axes1.plot(x, y4, label="Runge-Kutta", color='#d62728')
        self.axes1.legend()

        self.axes2.clear()
        self.axes2.set_title('Local approximation error')
        # n = 25
        x = ex.x_list(n)
        y1 = ex.pointwise_error(n)
        y2 = eu.pointwise_error(n)
        y3 = ieu.pointwise_error(n)
        y4 = rk.pointwise_error(n)
        if self.isExact:
            self.axes2.plot(x, y1, label="Exact", color='#1f77b4')
        if self.isEuler:
            self.axes2.plot(x, y2, label="Euler", color='#ff7f0e')
        if self.isImprovedEuler:
            self.axes2.plot(x, y3, label="Improved Euler", color='#2ca02c')
        if self.isRungeKutta:
            self.axes2.plot(x, y4, label="Runge-Kutta", color='#d62728')
        self.axes2.legend()

        self.axes3.clear()
        self.axes3.set_title('Total approximation error')
        # n_i = 10
        # n_f = 51
        n_i = self.n_i
        n_f = self.n_f
        x = np.arange(n_i, n_f)
        y1 = ex.total_approximation_error(n_i, n_f)
        y2 = eu.total_approximation_error(n_i, n_f)
        y3 = ieu.total_approximation_error(n_i, n_f)
        y4 = rk.total_approximation_error(n_i, n_f)
        # self.axes3.plot(x, y1, label="Exact", color='#1f77b4')
        if self.isEuler:
            self.axes3.plot(x, y2, label="Euler", color='#ff7f0e')
        if self.isImprovedEuler:
            self.axes3.plot(x, y3, label="Improved Euler", color='#2ca02c')
        if self.isRungeKutta:
            self.axes3.plot(x, y4, label="Runge-Kutta", color='#d62728')
        self.axes3.legend()
