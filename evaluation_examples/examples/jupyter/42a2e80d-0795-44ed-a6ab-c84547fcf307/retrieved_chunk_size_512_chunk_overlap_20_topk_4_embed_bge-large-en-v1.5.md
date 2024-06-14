Documentation Source:
jupyterlab.readthedocs.io/en/4.1.x/user/notebook.md

Documentation Title:
Notebooks — JupyterLab 4.1.8 documentation

Documentation Content:
However, a
number of new things are possible with notebooks in JupyterLab.

Drag and drop cells to rearrange your notebook:

Drag cells between notebooks to quickly copy content:

Create multiple synchronized views of a single notebook:

Collapse and expand code and output using the View menu or the blue
collapser button on left of each cell:

Enable scrolling for long outputs by right-clicking on a cell and
selecting “Enable Scrolling for Outputs”:

Create a new synchronized view of a cell’s output:

Tab completion (activated with the Tabkey) can now include additional
information about the types of the matched items:

Note: IPython 6.3.1 has temporarily disabled type annotations.
To re-enable them, add `c.Completer.use_jedi=True`to an
ipython\_config.pyfile.

The tooltip (activated with `ShiftTab`) contains additional
information about objects:

You can connect a code consoleto a notebook kernel to have a log of
computations done in the kernel, in the order in which they were done.
The attached code console also provides a place to interactively inspect
kernel state without changing the notebook. Right-click on a notebook
and select “New Console for Notebook”:

You can iterate through the kernel history in a document cell using `AltUp-Arrow`and `AltDown-Arrow`. To use this feature, enable kernel history access in the notebook settings.

Cell Toolbar#
-------------

If there is enough room for it, each cell has a toolbar that provides quick access to
commonly-used functions. If you would like to disable the cell toolbar, run:


```
jupyterlabextensiondisable@jupyterlab/cell-toolbar-extension

```
on the command line. You can enable it again by running:



Documentation Source:
jupyterlab.readthedocs.io/en/4.1.x/api/functions/notebook.NotebookActions.duplicate.md

Documentation Title:
duplicate | @jupyterlab

Documentation Content:
Parameters


	+ ##### notebook: Notebook
	
	The target notebook widget.
	+ ##### `Optional`mode: "replace"| "above"| "below"| "belowSelected"
	
	the mode of adding cells:
	 'below' (default) adds cells below the active cell,
	 'belowSelected' adds cells below all selected cells,
	 'above' adds cells above the active cell, and
	 'replace' removes the currently selected cells and adds cells in their place.
	
	NotesThe last pasted cell becomes the active cell.
	This is a no-op if there is no cell data on the clipboard.
	This action can be undone.#### Returns void
* Defined in packages/notebook/lib/actions.d.ts:436



Documentation Source:
jupyterlab.readthedocs.io/en/4.1.x/api/functions/notebook.NotebookActions.paste.md

Documentation Title:
paste | @jupyterlab

Documentation Content:
Parameters


	+ ##### notebook: Notebook
	
	The target notebook widget.
	+ ##### `Optional`mode: "replace"| "above"| "below"| "belowSelected"
	
	the mode of adding cells:
	 'below' (default) adds cells below the active cell,
	 'belowSelected' adds cells below all selected cells,
	 'above' adds cells above the active cell, and
	 'replace' removes the currently selected cells and adds cells in their place.
	
	NotesThe last pasted cell becomes the active cell.
	This is a no-op if there is no cell data on the clipboard.
	This action can be undone.#### Returns void
* Defined in packages/notebook/lib/actions.d.ts:419



Documentation Source:
jupyterlab.readthedocs.io/en/4.1.x/api/functions/notebook.NotebookActions.copy.md

Documentation Title:
copy | @jupyterlab

Documentation Content:
OptionsIEditorMimeTypeServicedefaultMimeTypeJSONEditorIOptionsLineColModelCodeEditorWrapperCodeViewerWidgetJSONEditorLineColIEditorFactoryServiceIEditorMimeTypeServiceIEditorServicesIPositionModelCOMPLETER\_ACTIVE\_CLASSCOMPLETER\_ENABLED\_CLASSIEditorServicesIPositionModelcodemirrorCodeMirrorEditorIOptionsEditorExtensionRegistrycreateConditionalExtensioncreateConfigurableExtensioncreateImmutableExtensiongetDefaultExtensionsEditorLanguageRegistrygetDefaultLanguageslegacyE



