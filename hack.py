#!/usr/bin/python

# calculator.py

import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):

        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(300, 250))
        self.formula = False
        menubar = wx.MenuBar()
        file = wx.Menu()
        file.Append(22, '&Quit', 'Exit Calculator')
        menubar.Append(file, '&File')
        self.SetMenuBar(menubar)
        wx.EVT_MENU(self, 22, self.OnClose)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.display = wx.TextCtrl(self, -1, '',  style=wx.TE_RIGHT)
        sizer.Add(self.display, 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 4)

        gs = wx.GridSizer(4, 4, 3, 3)
        gs.AddMany([(wx.Button(self, 20, 'Cls'), 0, wx.EXPAND),
                        
                         ])

        sizer.Add(gs, 1, wx.EXPAND)

        self.SetSizer(sizer)
        self.Centre()

        self.Bind(wx.EVT_BUTTON, self.OnClear, id=20)
        
    def OnClear(self, event):
        self.display.Clear()

    def OnBackspace(self, event):
        formula = self.display.GetValue()
        self.display.Clear()
        self.display.SetValue(formula[:-1])

    def OnClose(self, event):
        self.Close()

    def OnDivide(self, event):
        if self.formula:
            return
        self.display.AppendText('/')


    

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, 'calculator.py')
        frame.Show(True)
        self.SetTopWindow(frame)
        return True

app = MyApp(0)
app.MainLoop()