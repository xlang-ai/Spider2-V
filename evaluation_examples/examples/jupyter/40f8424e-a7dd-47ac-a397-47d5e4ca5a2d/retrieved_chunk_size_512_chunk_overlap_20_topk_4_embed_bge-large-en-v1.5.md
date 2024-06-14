Documentation Source:
jupyterlab.readthedocs.io/en/4.1.x/user/interface.md

Documentation Title:
The JupyterLab Interface — JupyterLab 4.1.8 documentation

Documentation Content:
JupyterLab extensionscan also create new top-level menus in the menu
bar.

Left and Right Sidebar#
-----------------------

The left sidebar contains a number of commonly-used tabs including:

a file browser,

a list of tabs in the main work and of running kernels and terminals,

the command palette (in 3.0+ moved to a modal window accessible with a keyboard shortcut),

the table of contents,

the extension manager.


!The right sidebar contains:

the property inspector (active in notebooks),

the debugger.


!The column that allows to switch between tabs is called Activity Bar in JupyterLab.

The sidebars can be collapsed or expanded by selecting “Show Left Sidebar”
or “Show Right Sidebar” in the View menu or by clicking on the active sidebar tab:

The location of tabs can be switched between the left and the right sidebar from the context menu.

JupyterLab extensions can add additional panels to the sidebars.

Main Work Area#
---------------

The main work area in JupyterLab enables you to arrange documents (notebooks,
text files, etc.) and other activities (terminals, code consoles, etc.) into
panels of tabs that can be resized or subdivided. Drag a tab to the center of a
tab panel to move the tab to the panel. Subdivide a tab panel by dragging a tab to
the left, right, top, or bottom of the panel:

The work area has a single current activity. The tab for the current activity is
marked with a colored top border (blue by default).

Tabs and Simple Interface Mode#
-------------------------------

The Tabs panel in the left sidebar lists the open documents or
activities in the main work area:

!The same information is also available in the Tabs menu:

!It is often useful to focus on a single document or activity without closing
other tabs in the main work area. Simple Interface mode enables this, while making
it easy to return to your multi-activity layout in the main work area.
Toggle Simple Interface mode using the View menu:

When you leave Simple Interface mode, the original layout of the main
area is restored.



Documentation Source:
jupyterlab.readthedocs.io/en/4.1.x/api/interfaces/ui_components.IInputGroupProps.md

Documentation Title:
IInputGroupProps | @jupyterlab

Documentation Content:
raria-posinsetaria-pressedaria-readonlyaria-relevantaria-requiredaria-roledescriptionaria-rowcountaria-rowindexaria-rowspanaria-selectedaria-setsizearia-sortaria-valuemaxaria-valueminaria-valuenowaria-valuetextautoCapitalizeautoCompleteautoCorrectautoFocusautoSavecapturecheckedchildrenclassNamecolorcontentEditablecontextMenucrossOrigindangerouslySetInnerHTMLdatatypedefaultCheckeddefaultValuedirdisableddraggableenterKeyHintformformActionformEncTypeformMethodformNoValidatef



Documentation Source:
jupyterlab.readthedocs.io/en/4.1.x/api/enums/notebook.RunningStatus.md

Documentation Title:
RunningStatus | @jupyterlab

Documentation Content:
Enumeration Members

ErrorIdleRunningScheduledEnumeration Members
-------------------

ErrorError:-0.5Cell execution is unsuccessful

- Defined in packages/notebook/lib/toc.d.ts:19
IdleIdle:-1Cell is idle

- Defined in packages/notebook/lib/toc.d.ts:15
RunningRunning:1Cell is running

- Defined in packages/notebook/lib/toc.d.ts:27
ScheduledScheduled:0Cell execution is scheduled

- Defined in packages/notebook/lib/toc.d.ts:23



Documentation Source:
jupyterlab.readthedocs.io/en/4.1.x/api/interfaces/apputils.Dialog.IBodyWidget.md

Documentation Title:
IBodyWidget | @jupyterlab

Documentation Content:
kerIMarkdownViewerTrackermathjax-extensionMathJaxTypesetterdefaultnbformatIAttachmentsIBaseCellIBaseCellJupyterMetadataIBaseCellMetadataIBaseOutputICodeCellICodeCellJupyterMetadataICodeCellMetadataIDisplayDataIDisplayUpdateIErrorIExecuteResultIKernelspecMetadataILanguageInfoMetadataIMarkdownCellIMimeBundleINotebookContentINotebookMetadataIRawCellIRawCellMetadataIStreamIUnrecognizedCellIUnrecognizedOutputCellTypeExecutionCountICellICellMetadataIOutputMultilineStringOutpu



