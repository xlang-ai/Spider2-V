Documentation Source:
jupyterlab.readthedocs.io/en/4.1.x/api/functions/services.TerminalAPI.startNew.md

Documentation Title:
startNew | @jupyterlab

Documentation Content:
MLSearchEngineSearchDocumentModelSearchDocumentViewSearchProviderSearchProviderRegistryIBaseSearchProviderIDisplayStateIFilterIFiltersIHTMLSearchMatchIReplaceOptionsIReplaceOptionsSupportISearchKeyBindingsISearchMatchISearchProviderISearchProviderFactoryISearchProviderRegistrySelectionStateFOUND\_CLASSESISearchProviderRegistryTextSearchEnginedocumentsearch-extensiondefaultextensionmanagerExtensionsPanelIOptionsListModelentryHasUpdateExtensionsPanelListModelIActionOptionsI



Documentation Source:
jupyterlab.readthedocs.io/en/4.1.x/api/functions/services.TerminalAPI.startNew.md

Documentation Title:
startNew | @jupyterlab

Documentation Content:
GitHubJupyter* Preparing search index...
* The search index is not available

@jupyterlab@jupyterlabservicesTerminalAPIstartNew
Function startNew
=================

* startNew(settings?, name?, cwd?): Promise
* Start a new terminal session.



Documentation Source:
jupyterlab.readthedocs.io/en/4.1.x/api/functions/services.KernelAPI.startNew.md

Documentation Title:
startNew | @jupyterlab

Documentation Content:
earchEngineSearchDocumentModelSearchDocumentViewSearchProviderSearchProviderRegistryIBaseSearchProviderIDisplayStateIFilterIFiltersIHTMLSearchMatchIReplaceOptionsIReplaceOptionsSupportISearchKeyBindingsISearchMatchISearchProviderISearchProviderFactoryISearchProviderRegistrySelectionStateFOUND\_CLASSESISearchProviderRegistryTextSearchEnginedocumentsearch-extensiondefaultextensionmanagerExtensionsPanelIOptionsListModelentryHasUpdateExtensionsPanelListModelIActionOptionsIAct



Documentation Source:
jupyterlab.readthedocs.io/en/4.1.x/getting_started/issue.md

Documentation Title:
Reporting an issue — JupyterLab 4.1.8 documentation

Documentation Content:
Skip to main contentBack to top
 `Ctrl`+`K`!Get StartedUser GuideDevelop ExtensionsContributePrivacy policies!GitHubDiscourseGitterGet StartedUser GuideDevelop ExtensionsContributePrivacy policies!GitHubDiscourseGitterSection Navigation

InstallationStarting JupyterLabReporting an issueFrequently Asked Questions (FAQ)JupyterLab ChangelogJupyterLab Accessibility StatementVersion lifecycleGet Started* Reporting an issue

Reporting an issue#
===================

Thank you for providing feedback about JupyterLab.

Diagnosing an Issue#
--------------------

If you find a problem in JupyterLab, please follow the steps below to diagnose and report the issue. Following these steps helps you diagnose if the problem is likely from JupyterLab or from a different project.

1. Try to reproduce the issue in a new environment with the latest official JupyterLab installed and no extra packages.

If you are using conda:


	1. create a new environment:
	
	
	```
	condacreate-njlab-test--override-channels--strict-channel-priority-cconda-forge-cnodefaultsjupyterlab
	```
	2. Activate the environment:
	
	
	```
	condaactivatejlab-test
	```
	3. Start JupyterLab:
	
	
	```
	jupyterlab
	```
	I cannot reproduce this issue in a clean environment: The problem is probably not in JupyterLab itself. Go to step 2.
	
	I can reproduce this issue in a clean environment: Go to step 3.
2. Perhaps the issue is in one of the JupyterLab extensions you had installed. Install any JupyterLab extensions you had one at a time, checking for the issue after each one.



