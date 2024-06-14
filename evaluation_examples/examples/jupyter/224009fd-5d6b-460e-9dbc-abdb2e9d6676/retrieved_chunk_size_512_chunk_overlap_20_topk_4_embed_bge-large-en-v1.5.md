Documentation Source:
jupyterlab.readthedocs.io/en/4.1.x/api/functions/notebook.NotebookActions.mergeCells.md

Documentation Title:
mergeCells | @jupyterlab

Documentation Content:
Parameters


	+ ##### notebook: Notebook
	
	The target notebook widget.
	+ ##### `Optional`mergeAbove: boolean
	
	If only one cell is selected, indicates whether to merge it
	 with the cell above (true) or below (false, default).
	
	NotesThe widget mode will be preserved.
	If only one cell is selected and `mergeAbove`is true, the above cell will be selected.
	If only one cell is selected and `mergeAbove`is false, the below cell will be selected.
	If the active cell is a code cell, its outputs will be cleared.
	This action can be undone.
	The final cell will have the same type as the active cell.
	If the active cell is a markdown cell, it will be unrendered.#### Returns void
* Defined in packages/notebook/lib/actions.d.ts:117



Documentation Source:
jupyterlab.readthedocs.io/en/4.1.x/api/functions/notebook.NotebookActions.runAndAdvance.md

Documentation Title:
runAndAdvance | @jupyterlab

Documentation Content:
Parameters


	+ ##### notebook: Notebook
	
	The target notebook widget.
	+ ##### `Optional`sessionContext: ISessionContext
	
	The client session object.
	+ ##### `Optional`sessionDialogs: ISessionContextDialogs
	
	The session dialogs.
	+ ##### `Optional`translator: ITranslator
	
	The application translator.
	
	NotesThe existing selection will be cleared.
	The cell after the last selected cell will be activated and scrolled into view.
	An execution error will prevent the remaining code cells from executing.
	All markdown cells will be rendered.
	If the last selected cell is the last cell, a new code cell
	will be created in `'edit'`mode. The new cell creation can be undone.#### Returns Promise
* Defined in packages/notebook/lib/actions.d.ts:226



Documentation Source:
jupyterlab.readthedocs.io/en/4.1.x/api/functions/notebook.NotebookActions.runAllBelow.md

Documentation Title:
runAllBelow | @jupyterlab

Documentation Content:
Parameters


	+ ##### notebook: Notebook
	
	The target notebook widget.
	+ ##### `Optional`sessionContext: ISessionContext
	
	The client session object.
	+ ##### `Optional`sessionDialogs: ISessionContextDialogs
	
	The session dialogs.
	+ ##### `Optional`translator: ITranslator
	
	The application translator.
	
	NotesThe existing selection will be cleared.
	An execution error will prevent the remaining code cells from executing.
	All markdown cells will be rendered.
	The last cell in the notebook will be activated and scrolled into view.#### Returns Promise
* Defined in packages/notebook/lib/actions.d.ts:289



Documentation Source:
jupyterlab.readthedocs.io/en/4.1.x/api/classes/console.CodeConsole-1.md

Documentation Title:
CodeConsole | @jupyterlab

Documentation Content:
Returns void
* Defined in packages/console/lib/widget.d.ts:126
serialize* serialize(): ICodeCell[]
* Serialize the output.

NotesThis only serializes the code cells and the prompt cell if it exists, and
skips any old banner cells.



