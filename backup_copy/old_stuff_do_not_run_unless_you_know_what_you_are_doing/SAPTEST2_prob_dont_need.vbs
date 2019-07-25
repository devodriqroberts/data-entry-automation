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
session.findById("wnd[0]").maximize
session.findById("wnd[0]/tbar[0]/okcd").text = "mm01"
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/usr/ctxtRMMG1-MATNR").text = "123456789"
session.findById("wnd[0]/usr/cmbRMMG1-MBRSH").key = "M"
session.findById("wnd[0]/usr/cmbRMMG1-MTART").key = "HALB"
session.findById("wnd[0]/usr/ctxtRMMG1_REF-MATNR").text = "PURHALBTEMP"
session.findById("wnd[0]/usr/ctxtRMMG1_REF-MATNR").setFocus
session.findById("wnd[0]/usr/ctxtRMMG1_REF-MATNR").caretPosition = 11
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[1]/usr/ctxtRMMG1-WERKS").text = "6000"
session.findById("wnd[1]/usr/ctxtRMMG1-VKORG").text = "1600"
session.findById("wnd[1]/usr/ctxtRMMG1-VTWEG").text = "10"
session.findById("wnd[1]/usr/ctxtRMMG1_REF-WERKS").text = "6000"
session.findById("wnd[1]/usr/ctxtRMMG1_REF-VKORG").text = "1600"
session.findById("wnd[1]/usr/ctxtRMMG1_REF-VTWEG").text = "10"
session.findById("wnd[1]/usr/ctxtRMMG1_REF-VTWEG").setFocus
session.findById("wnd[1]/usr/ctxtRMMG1_REF-VTWEG").caretPosition = 2
session.findById("wnd[1]").sendVKey 0
session.findById("wnd[0]/usr/tabsTABSPR1/tabpSP01/ssubTABFRA1:SAPLMGMM:2004/subSUB1:SAPLMGD1:1002/txtMAKT-MAKTX").text = "THIS IS A TEST"
session.findById("wnd[0]/usr/tabsTABSPR1/tabpSP01/ssubTABFRA1:SAPLMGMM:2004/subSUB1:SAPLMGD1:1002/txtMAKT-MAKTX").caretPosition = 14
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
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[1]/usr/btnSPOP-OPTION1").press
session.findById("wnd[0]/tbar[0]/btn[12]").press
