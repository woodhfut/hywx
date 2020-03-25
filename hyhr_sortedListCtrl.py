import wx
import wx.lib.mixins.listctrl
# actresses = {
# 1 : ('Jessica Alba', 'Pomona', '1981'),
# 2 : ('Sigourney Weaver', 'New York', '1949'),
# 3 : ('Angelina Jolie', 'Los Angeles', '1975'),
# 4 : ('Natalie Portman', 'Jerusalem', '1981'),
# 5 : ('Rachel Weiss', 'London', '1971'),
# 6 : ('Scarlett Johansson', 'New York', '1984')
# }

class SortedListCtrl(wx.ListCtrl, wx.lib.mixins.listctrl.ColumnSorterMixin):

    def __init__(self, colCount, datamap, *args, **kwargs):

        wx.ListCtrl.__init__(self, *args, **kwargs)
        wx.lib.mixins.listctrl.ColumnSorterMixin.__init__(self, colCount)
        self.itemDataMap = datamap
    
    # def SetItemDataMap(self, datamap):
    #     self.itemDataMap = datamap

    def GetListCtrl(self):
        return self


# class Example(wx.Frame):

#     def __init__(self, *args, **kw):
#         super(Example, self).__init__(*args, **kw)

#         self.InitUI()

#     def InitUI(self):

#         hbox = wx.BoxSizer(wx.HORIZONTAL)
#         panel = wx.Panel(self)

#         self.list = SortedListCtrl(3,{},panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 480,300 ),style=wx.LC_REPORT)
#         self.list.InsertColumn(0, 'name', width=140)
#         self.list.InsertColumn(1, 'place', width=130)
#         self.list.InsertColumn(2, 'year', wx.LIST_FORMAT_RIGHT, 90)

#         items = actresses.items()

#         idx = 0

#         for key, data in items:

#             index = self.list.InsertItem(idx, data[0])
#             self.list.SetItem(index, 1, data[1])
#             self.list.SetItem(index, 2, data[2])
#             self.list.SetItemData(index, key)
#             self.list.itemDataMap[index]= actresses[key]
#             idx += 1

#         hbox.Add(self.list, 1, wx.EXPAND)
#         panel.SetSizer(hbox)

#         self.SetTitle('Actresses')
#         self.Centre()


# def main():

#     app = wx.App()
#     ex = Example(None)
#     ex.Show()
#     app.MainLoop()


# if __name__ == '__main__':
#     main()