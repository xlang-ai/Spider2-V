Documentation Source:
www.metabase.com/docs/v0.49/people-and-groups/api-keys.md

Documentation Title:
API keys

Documentation Content:
when!Analytics dashboards
 Share insights with anyone, anywhere!SQL editor
 For advanced data users!Sandboxing
 Set boundaries around your data!Models
 A starting point for questions!Permissions
 Keep your data secure and private!CSV upload
 Go beyond VLOOKUPDocumentationResources!Learn!Blog!Events!Customers!Discussion!Partners!Community Stories!Startup Guide to Financial Modeling
 New!Community Data Stack Report
 NewPricingLog inv0.49People and Groups
API keys
========

Metabase can create API keys to authenticate programmatic requests to the API. To set the permissions for an API key, you can assign the key to a group.

Fair warning about Metabase’s API
---------------------------------

We don’t version the Metabase API. We rarely change API endpoints, and almost never remove them, but if you write code that relies on the API, there’s a chance you might have to update your code in the future.

That said, there are times when it’s nice to work with the API, like when managing permissions with a large number of people and groups, or bulk archiving, or content creation. So we added the ability to create API keys to authenticate your programmatic requests.

Create an API key
-----------------

To create an API key:

1. Click on the **gear**icon in the upper right.
2. Select **Admin settings**.
3. Go to the **Settings**tab.
4. Click on the **Authentication**tab on the left menu.
5. Scroll to **API Keys**and click **Manage**.
6. Click the **Create API Key**button.
7. Enter a **Key name**. You can have multiple API keys, so give it a name that will help you remember what you’re using the key for.
8. Select a Group. The key will have the same permissions granted to that group.
9. Click **Create**.
10. Copy the generated API key and save it somewhere safe. Metabase won’t be able to show you the key again. If you lose the key, you’ll need to regenerate a new key.

Managing API Keys
-----------------

To view and manage existing API keys:

1. Click on the **gear**icon in the upper right.
2.



Documentation Source:
www.metabase.com/docs/v0.49/api/api-key.md

Documentation Title:
API key

Documentation Content:
PARAMS:

`_body``POST /api/api-key/`Create a new API key (and an associated `User`) with the provided name and group ID.

You must be a superuser to do this.



Documentation Source:
www.metabase.com/docs/v0.49/installation-and-operation/serialization.md

Documentation Title:
Serialization

Documentation Content:
Step 1: Set up an API key

1. Create an API key.
2. Assign the key to the Admin group



Documentation Source:
www.metabase.com/docs/v0.49/people-and-groups/api-keys.md

Documentation Title:
API keys

Documentation Content:
`curl`example

Replace `YOUR_API_KEY`with the API key you generated above.

`curl \-H'x-api-key: YOUR_API_KEY'\-XGET 'http://localhost:3000/api/permissions/group'`### JavaScript example

Assuming you’ve set your key as an environment variable like so:

`export METABASE_API_KEY="YOUR_API_KEY"`Here’s a basic `GET`request using `fetch`to get the list of groups. You can copy the code, save it as file (e.g., as `api-test.js`), and run the code with `node api-test.js`.

`// Assuming you've set the key in process with// `export METABASE_API_KEY="YOUR_KEY_HERE"`constAPI_KEY=process.env.METABASE_API_KEY;constinit={headers:{"Content-Type":"application/json","X-API-KEY":API_KEY,},};consthost="http://127.0.0.1:3000";asyncfunctiongetGroups(){constresponse=awaitfetch(`${host}/api/permissions/group`,init);returnresponse.json();}getGroups().then(groups=>console.log("Groups in your Metabase:",groups));`Further reading
---------------

* Metabase API reference.
* Working with the Metabase API.
Read docs for other versions of Metabase.
 

Did this article help you?
 

Yes
 No
 Send
 Thanks for your feedback!

Want to improve these docs? Propose a change.##### Subscribe to our newsletter

Stay in touch with updates and news from Metabase. No spam, ever.



