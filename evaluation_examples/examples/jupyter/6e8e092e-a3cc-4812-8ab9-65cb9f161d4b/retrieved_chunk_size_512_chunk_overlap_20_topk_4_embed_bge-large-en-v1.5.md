Documentation Source:
jupyterlab.readthedocs.io/en/4.1.x/api/interfaces/statedb.IObjectPool.md

Documentation Title:
IObjectPool | @jupyterlab

Documentation Content:
UtilsMarkdownIMarkdownHeadinggetHeadingIdgetHeadingsisMarkdownIHTMLHeadingNUMBERING\_CLASSaddPrefixclearNumberingfilterHeadingsgetHTMLHeadingsgetPrefixisHTMLTableOfContentsFactoryTableOfContentsItemTableOfContentsModelTableOfContentsPanelTableOfContentsRegistryTableOfContentsTrackerTableOfContentsTreeTableOfContentsWidgetITableOfContentsItemsPropsITableOfContentsRegistryITableOfContentsTrackerITableOfContentsTreePropsITableOfContentsRegistryITableOfContentsTrackertooltip



Documentation Source:
jupyterlab.readthedocs.io/en/4.1.x/api/interfaces/filebrowser.IUploadModel.md

Documentation Title:
IUploadModel | @jupyterlab

Documentation Content:
ayUpdateIErrorIExecuteResultIKernelspecMetadataILanguageInfoMetadataIMarkdownCellIMimeBundleINotebookContentINotebookMetadataIRawCellIRawCellMetadataIStreamIUnrecognizedCellIUnrecognizedOutputCellTypeExecutionCountICellICellMetadataIOutputMultilineStringOutputMetadataOutputTypeStreamTypeMAJOR\_VERSIONMINOR\_VERSIONisCodeisDisplayDataisDisplayUpdateisErrorisExecuteResultisMarkdownisRawisStreamvalidateMimeValuenotebookCommandEditStatusModelExecutionIndicatorModelIExecutionS



Documentation Source:
jupyterlab.readthedocs.io/en/4.1.x/user/urls.md

Documentation Title:
JupyterLab URLs — JupyterLab 4.1.8 documentation

Documentation Content:
```
$# Exports the default JupyterLab workspace$jupyterlabworkspacesexport{"data":{},"metadata":{"id":"/lab"}}$
$# Exports the workspaces named `foo`$jupyterlabworkspacesexportfoo
{"data":{},"metadata":{"id":"/lab/workspaces/foo"}}$
$# Exports the workspace named `foo` into a file called `file_name.json`$jupyterlabworkspacesexportfoo>file_name.json
$
$# Imports the workspace file `file_name.json`.$jupyterlabworkspacesimportfile_name.json
Savedworkspace:/labworkspacesfoo-54d5.jupyterlab-workspace

```
The exportfunctionality is as friendly as possible: if a workspace does not
exist, it will still generate an empty workspace for export.

The importfunctionality validates the structure of the workspace file and
validates the idfield in the workspace metadatato make sure its URL is
compatible with either the workspaces\_urlconfiguration or the page\_urlconfiguration to verify that it is a correctly named workspace or it is the
default workspace.

Workspace File Format#
----------------------

A workspace file is a JSON file with a specific spec.

There are two top level keys requires, data, and metadata.

The metadatamust be a mapping with an idkey that has the same value as the ID of the workspace. This should also be the relative URL path to access the workspace,
like /lab/workspaces/foo.

The datakey maps to the initial state of the IStateDB. Many plugins look in the State DB for the configuration.
Also any plugins that register with the ILayoutRestorerwill look up all keys in the State DB
that start with the namespaceof their tracker before the first :. The values of these keys should have a dataattribute that maps.

For example, if your workspace looks like this:


```
{"data":{"application-mimedocuments:package.json:JSON":{"data":{"path":"package.json","factory":"JSON"}}}}
```
It will run the docmanager:openwith the { “path”: “package.json”, “factory”: “JSON” }args, because the application-mimedocumentstracker is registered with the docmanager:opencommand, like this:



Documentation Source:
jupyterlab.readthedocs.io/en/4.1.x/api/interfaces/filebrowser.IUploadModel.md

Documentation Title:
IUploadModel | @jupyterlab

Documentation Content:
lRawCellModelIAttachmentsCellModelICellFooterICellHeaderICellModelICodeCellModelIInputPromptIMarkdownCellModelIPlaceholderOptionsIRawCellModelSELECTED\_HIGHLIGHT\_CLASScreateCellSearchProviderisCodeCellModelisMarkdownCellModelisRawCellModelcodeeditorCodeEditorModelIOptionsModelICoordinateIDimensionIEditorIModelIOptionsIPositionIRangeISelectionOwnerITextSelectionITokenEdgeLocationFactoryKeydownHandlerCodeEditorWrapperIOptionsCodeViewerWidgetINoModelOptionsIOptionsIEditorMi



