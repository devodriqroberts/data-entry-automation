If Not IsObject(application) Then
   Set SapGuiAuto  = GetObject("SAPGUI")
   Set application = SapGuiAuto.GetScriptingEngine
End If
If Not IsObject(connection) Then
   Set connection = application.Children(0)
End If
If Not IsObject(session) Then
   Set session    = connection.Children(0)
End If
If IsObject(WScript) Then
   WScript.ConnectObject session,     "on"
   WScript.ConnectObject application, "on"
End If


materialnumber = WScript.Arguments.Item(0)
description = WScript.Arguments.Item(1)
distributionchannel = WScript.Arguments.Item(2)
salesorg = WScript.Arguments.Item(3)
' plant = WScript.Arguments.Item(4)


session.findById("wnd[0]").maximize
session.findById("wnd[0]/tbar[0]/okcd").text = "mm01"
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/usr/ctxtRMMG1-MATNR").text = materialnumber
session.findById("wnd[0]/usr/cmbRMMG1-MBRSH").key = "M"
session.findById("wnd[0]/usr/cmbRMMG1-MTART").key = "HALB"
session.findById("wnd[0]/usr/ctxtRMMG1_REF-MATNR").text = "SVCPURTEMP"
session.findById("wnd[0]/usr/ctxtRMMG1_REF-MATNR").setFocus
' session.findById("wnd[0]/usr/ctxtRMMG1_REF-MATNR").caretPosition = 10
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[1]/usr/ctxtRMMG1-WERKS").text = "6001"
session.findById("wnd[1]/usr/ctxtRMMG1-VKORG").text = salesorg
session.findById("wnd[1]/usr/ctxtRMMG1-VTWEG").text = distributionchannel

' these are the "copy from" area so they are hard coded
session.findById("wnd[1]/usr/ctxtRMMG1_REF-WERKS").text = "6001"
session.findById("wnd[1]/usr/ctxtRMMG1_REF-VKORG").text = "1600"
session.findById("wnd[1]/usr/ctxtRMMG1_REF-VTWEG").text = "40"
session.findById("wnd[1]/usr/ctxtRMMG1_REF-VTWEG").setFocus
session.findById("wnd[1]/usr/ctxtRMMG1_REF-VTWEG").caretPosition = 2
session.findById("wnd[1]").sendVKey 0
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/usr/tabsTABSPR1/tabpSP02/ssubTABFRA1:SAPLMGMM:2004/subSUB1:SAPLMGD1:1002/txtMAKT-MAKTX").text = "TESTING AGAIN"
session.findById("wnd[0]/usr/tabsTABSPR1/tabpSP02/ssubTABFRA1:SAPLMGMM:2004/subSUB1:SAPLMGD1:1002/txtMAKT-MAKTX").caretPosition = 14
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/usr/tabsTABSPR1/tabpSP13/ssubTABFRA1:SAPLMGMM:2000/subSUB2:SAPLMGD1:2484/ctxtMARC-BESKZ").text = "F"
session.findById("wnd[0]/usr/tabsTABSPR1/tabpSP13/ssubTABFRA1:SAPLMGMM:2000/subSUB2:SAPLMGD1:2484/ctxtMARC-BESKZ").setFocus
session.findById("wnd[0]/usr/tabsTABSPR1/tabpSP13/ssubTABFRA1:SAPLMGMM:2000/subSUB2:SAPLMGD1:2484/ctxtMARC-BESKZ").caretPosition = 1
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[1]/usr/btnSPOP-OPTION1").press
session.findById("wnd[0]/tbar[0]/btn[15]").press
