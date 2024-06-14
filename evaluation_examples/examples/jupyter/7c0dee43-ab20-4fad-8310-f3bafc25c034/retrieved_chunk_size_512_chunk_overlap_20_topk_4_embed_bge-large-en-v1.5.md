Documentation Source:
jupyterlab.readthedocs.io/en/4.1.x/api/functions/notebook.NotebookActions.showOutput.md

Documentation Title:
showOutput | @jupyterlab

Documentation Content:
GitHubJupyter* Preparing search index...
* The search index is not available

@jupyterlab@jupyterlabnotebookNotebookActionsshowOutput
Function showOutput
===================

* showOutput(notebook): void
* Show the output on selected code cells.



Documentation Source:
jupyterlab.readthedocs.io/en/4.1.x/api/classes/notebook.NotebookViewModel.md

Documentation Title:
NotebookViewModel | @jupyterlab

Documentation Content:
Returns number

Total estimated size

Inherited from WindowedListModel.getEstimatedTotalSize

* Defined in packages/ui-components/lib/components/windowedlist.d.ts:113
getOffsetForIndexAndAlignment* getOffsetForIndexAndAlignment(index, align?, margin?, precomputed?, alignPreference?): number
* Get the scroll offset to display an item in the viewport.

By default, the list will scroll as little as possible to ensure the item is fully visible (`auto`).
You can control the alignment of the item though by specifying a second alignment parameter.
Acceptable values are:

auto - Automatically align with the top or bottom minimising the amount scrolled,
 If `alignPreference`is given, follow such preferred alignment.
 If item is smaller than the viewport and fully visible, do not scroll at all.
 smart - If the item is significantly visible, don't scroll at all (regardless of whether it fits in the viewport).
 If the item is less than one viewport away, scroll so that it becomes fully visible (following the `auto`heuristics).
 If the item is more than one viewport away, scroll so that it is centered within the viewport (`center`if smaller than viewport, `top-center`otherwise).
 center - Align the middle of the item with the middle of the viewport (it only works well for items smaller than the viewport).
 top-center - Align the top of the item with the middle of the viewport (works well for items larger than the viewport).
 end - Align the bottom of the item to the bottom of the list.
 start - Align the top of item to the top of the list.

An item is considered significantly visible if:


	+ it overlaps with the viewport by the amount specified by `scrollDownThreshold`when below the viewport
	+ it exceeds the viewport by the amount less than specified by `scrollUpThreshold`when above the viewport.#### Parameters



Documentation Source:
jupyterlab.readthedocs.io/en/4.1.x/api/functions/notebook.ExecutionIndicator.createExecutionIndicatorItem.md

Documentation Title:
createExecutionIndicatorItem | @jupyterlab

Documentation Content:
GitHubJupyter* Preparing search index...
* The search index is not available

@jupyterlab@jupyterlabnotebookExecutionIndicatorcreateExecutionIndicatorItem
Function createExecutionIndicatorItem
=====================================

* createExecutionIndicatorItem(panel, translator?, loadSettings?): Widget
* #### Parameters


	##### panel: NotebookPanel
	
	##### `Optional`translator: ITranslator
	
	##### `Optional`loadSettings: Promise#### Returns Widget
* Defined in packages/notebook/lib/executionindicator.d.ts:215



Documentation Source:
jupyterlab.readthedocs.io/en/4.1.x/api/classes/extensionmanager.ListModel-1.md

Documentation Title:
ListModel | @jupyterlab

Documentation Content:
Returns string
* Defined in packages/extensionmanager/lib/model.d.ts:174
* setquery(value): void
* #### Parameters



