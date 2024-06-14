Documentation Source:
jupyterlab.readthedocs.io/en/4.1.x/api/classes/csvviewer.DSVModel-1.md

Documentation Title:
DSVModel | @jupyterlab

Documentation Content:
Param

The last row to parse, from the start of the data (first
row is row 1).

NotesThis method supports parsing the data incrementally by calling it with
incrementally higher endRow. Rows that have already been parsed will not be
parsed again.

- Defined in packages/csvviewer/lib/model.d.ts:112



Documentation Source:
jupyterlab.readthedocs.io/en/4.1.x/api/types/csvviewer.IParser-1.md

Documentation Title:
IParser | @jupyterlab

Documentation Content:
Returns IResults

An object giving the offsets for the rows or columns parsed.

NotesThe parsers are based on RFC 4180.
* Defined in packages/csvviewer/lib/parse.d.ts:10
* Defined in packages/csvviewer/lib/parse.d.ts:11



Documentation Source:
jupyterlab.readthedocs.io/en/4.1.x/api/interfaces/csvviewer.IParser.IResults.md

Documentation Title:
IResults | @jupyterlab

Documentation Content:
PropsIStatusBarIItemAlignmentPopupIOptionsProgressBarIPropsProgressCircleIPropsTextItemIPropsPopupStatusBarIStatusBarIStatusBarGroupItemProgressBarProgressCircleTextItemshowPopupterminalITerminalIOptionsITerminalIThemeObjectThemedefaultOptionsTerminalITerminalTrackerITerminalTrackertocTableOfContentsIConfigIFactoryIHeadingIModelIOptionsIToolbarItemsModeldefaultConfigTableOfContentsUtilsMarkdownIMarkdownHeadinggetHeadingIdgetHeadingsisMarkdownIHTMLHeadingNUMBERING\_CLASSad



Documentation Source:
jupyterlab.readthedocs.io/en/4.1.x/api/classes/csvviewer.DSVModel-1.md

Documentation Title:
DSVModel | @jupyterlab

Documentation Content:
Returns number
* The row count for the region.
Overrides DataModel.rowCount

* Defined in packages/csvviewer/lib/model.d.ts:58



