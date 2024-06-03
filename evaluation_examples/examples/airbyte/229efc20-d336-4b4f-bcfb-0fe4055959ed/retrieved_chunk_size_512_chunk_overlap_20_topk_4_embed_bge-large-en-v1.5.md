Documentation Source:
airbyte.com/docs.airbyte.com/integrations/destinations/local-json.md

Documentation Title:
Local JSON | Airbyte Documentation

Documentation Content:
Features​



| Feature | Supported |
| --- | --- |
| Full Refresh Sync | Yes |
| --- | --- |
| Incremental - Append Sync | Yes |
| Incremental - Append + Deduped | No |
| Namespaces | No |



Documentation Source:
airbyte.com/docs.airbyte.com/integrations/destinations/local-json.md

Documentation Title:
Local JSON | Airbyte Documentation

Documentation Content:
Sync Overview​



Documentation Source:
airbyte.com/tutorials/extract-data-from-the-webflow-api.md

Documentation Title:
Build a connector to extract data from the Webflow API | Airbyte

Documentation Content:
Once this is done, you will see that the first sync has already started as follows: 

!‍

And after a few minutes, if everything has gone as expected, you should see that the connection succeeded as follows:

!‍

You can then look in the local directory at */tmp/airbyte\_local/webflow-blog-test*to verify that several json files have been created, with each file corresponding to a Webflow collection. In my case, the output looks as follows: 

!‍

This confirms that all of the collections have been pulled from Webflow, and copied to a directory on my local host!



Documentation Source:
airbyte.com/docs.airbyte.com/integrations/destinations/local-json.md

Documentation Title:
Local JSON | Airbyte Documentation

Documentation Content:
Example:​

* If `destination_path`is set to `/local/cars/models`
* the local mount is using the `/tmp/airbyte_local`default
* then all data will be written to `/tmp/airbyte_local/cars/models`directory.

Access Replicated Data Files​
-----------------------------

If your Airbyte instance is running on the same computer that you are navigating with, you can open your browser and enter file:///tmp/airbyte\_localto look at the replicated data locally. If the first approach fails or if your Airbyte instance is running on a remote server, follow the following steps to access the replicated files:

1. Access the scheduler container using `docker exec -it airbyte-server bash`
2. Navigate to the default local mount using `cd /tmp/airbyte_local`
3. Navigate to the replicated file directory you specified when you created the destination, using `cd /{destination_path}`
4. List files containing the replicated data using `ls`
5. Execute `cat {filename}`to display the data in a particular file

You can also copy the output file to your host machine, the following command will copy the file to the current working directory you are using:

docker cp airbyte-server:/tmp/airbyte\_local/{destination\_path}/{filename}.jsonl .Note: If you are running Airbyte on Windows with Docker backed by WSL2, you have to use similar step as above or refer to this linkfor an alternative approach.

Changelog​
----------



| Version | Date | Pull Request | Subject |
| --- | --- | --- | --- |
| 0.2.11 | 2022-02-14 |14641 Include lifecycle management |

Edit this pagePreviousVector Database (powered by LangChain) Migration GuideNextMariadb Columnstore* OverviewSync Overview
* Getting StartedExample:
Access Replicated Data FilesChangelog
Was this page helpful?YesNo



