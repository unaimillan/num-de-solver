# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"D.E. Assignment", pos = wx.DefaultPosition, size = wx.Size( 1135,717 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer3.AddGrowableCol( 1 )
        fgSizer3.AddGrowableRow( 0 )
        fgSizer3.SetFlexibleDirection( wx.BOTH )
        fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer4.SetFlexibleDirection( wx.BOTH )
        fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"x0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        fgSizer4.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble1 = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -100, 100, 0, 0.1 )
        self.m_spinCtrlDouble1.SetDigits( 3 )
        fgSizer4.Add( self.m_spinCtrlDouble1, 0, wx.ALL, 5 )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"y0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        fgSizer4.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble11 = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -100, 100, 0, 0.1 )
        self.m_spinCtrlDouble11.SetDigits( 3 )
        fgSizer4.Add( self.m_spinCtrlDouble11, 0, wx.ALL, 5 )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        fgSizer4.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrlDouble12 = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -100, 100, 3, 0.1 )
        self.m_spinCtrlDouble12.SetDigits( 3 )
        fgSizer4.Add( self.m_spinCtrlDouble12, 0, wx.ALL, 5 )

        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"N", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        fgSizer4.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl1 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 10000, 15 )
        fgSizer4.Add( self.m_spinCtrl1, 0, wx.ALL, 5 )

        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"N_i", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        fgSizer4.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl11 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 10000, 10 )
        fgSizer4.Add( self.m_spinCtrl11, 0, wx.ALL, 5 )

        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"N_f", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        fgSizer4.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl12 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 10000, 50 )
        fgSizer4.Add( self.m_spinCtrl12, 0, wx.ALL, 5 )


        bSizer3.Add( fgSizer4, 0, wx.EXPAND|wx.ALL, 5 )

        self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Soutions:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )

        bSizer3.Add( self.m_staticText10, 0, wx.ALL, 5 )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        self.m_checkBox5 = wx.CheckBox( self, wx.ID_ANY, u"Exact", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_checkBox5.SetValue(True)
        bSizer6.Add( self.m_checkBox5, 0, wx.ALL, 5 )

        self.m_checkBox6 = wx.CheckBox( self, wx.ID_ANY, u"Euler", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_checkBox6.SetValue(True)
        bSizer6.Add( self.m_checkBox6, 0, wx.ALL, 5 )

        self.m_checkBox7 = wx.CheckBox( self, wx.ID_ANY, u"Improved Euler", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_checkBox7.SetValue(True)
        bSizer6.Add( self.m_checkBox7, 0, wx.ALL, 5 )

        self.m_checkBox8 = wx.CheckBox( self, wx.ID_ANY, u"Runge-Kutta", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_checkBox8.SetValue(True)
        bSizer6.Add( self.m_checkBox8, 0, wx.ALL, 5 )


        bSizer3.Add( bSizer6, 0, wx.EXPAND|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

        self.button_calc = wx.Button( self, wx.ID_ANY, u"Calculate", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.button_calc, 0, wx.ALL, 5 )


        fgSizer3.Add( bSizer3, 1, wx.EXPAND, 5 )

        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4.Add( self.m_panel4, 1, wx.ALL|wx.EXPAND, 5 )


        fgSizer3.Add( bSizer4, 1, wx.EXPAND, 5 )


        self.SetSizer( fgSizer3 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.button_calc.Bind( wx.EVT_BUTTON, self.button_calcOnButtonClick )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def button_calcOnButtonClick( self, event ):
        event.Skip()


