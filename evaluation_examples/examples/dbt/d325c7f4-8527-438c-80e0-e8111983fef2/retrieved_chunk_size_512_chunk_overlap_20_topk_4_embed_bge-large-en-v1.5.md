Documentation Source:
docs.getdbt.com/blog/customer-360-view-identity-resolution.md

Documentation Title:
The JaffleGaggle Story: Data Modeling for a Customer 360 View | dbt Developer Blog

Documentation Content:
Step 2.1: Extract email domain from an email​

For this step, take a look at a snippet from `models/staging/stg_users.sql`below. In it, we **perform the email domain extraction from the email**.

`selectid as user_id,name as user_name,email,{{ extract_email_domain('email') }} AS email_domain,gaggle_id,created_atfrom source`We defined the email domain extraction as a macrocalled `extract_email_domain`, which we call in line 18 (which you can find in the pullout below).

This uses a regex to capture the text to the right of the ‘@’ character and makes sure to only use the lowercase email parameter before extracting the domain. This is because email domains aren’t case sensitive, but SQL is (see users 2954 and 3140 in the seed datafor an example).

`{% macro extract_email_domain(email) %}{# This is the SQL to extract the email domain in the Snowflake Flavor of SQL #}regexp_substr(lower({{ email }}), '@(.*)', 1, 1, 'e',1){% endmacro %}`Builder Beware! Notice we didn’t check for improperly formatted emails, like periods at the end of the domain or whitespaces. Make sure you check your dataset to see if this is a valid assumption.

Generally, it’d be useful to leverage a regular expression to strip and pull down an email address. However, because this is a B2B use case, not all email domains are created equal. We want to make sure we flag personal emails so they’re treated differently than the corporate emails our sales team will reach out to (this makes sales outreach more productive, and ensures we aren’t contacting people more than once).

**Tip:**If you’re building out a definition like "personal email domains" for the first time, I strongly recommend building alignment upfront with the rest of the business. . Understanding the impact and having a shared understanding of these kinds of definitions reduces friction and allows you to run your data team like a product teamrather than responding to ad hoc service requests.



Documentation Source:
docs.getdbt.com/docs/build/unit-tests.md

Documentation Title:
Unit tests | dbt Developer Hub

Documentation Content:
[A-Za-z]{2,}$'`(those pesky escape characters) and rerunning the unit test solves the problem:

`dbt test--selecttest_is_valid_email_address16:09:11 Running with dbt=1.8.0-a116:09:12 Registered adapter: postgres=1.8.0-a116:09:12 Found 6models, 5seeds, 4data tests, 0sources, 0exposures, 0metrics, 410macros, 0groups, 0semantic models, 1unit test16:09:12 16:09:13 Concurrency: 5threads (target='postgres')16:09:13 16:09:13 1of 1START unit_test dim_customers::test_is_valid_email_address ................... [RUN]16:09:13 1of 1PASS dim_customers::test_is_valid_email_address ..............................[PASS in0.26s]16:09:13 16:09:13 Finished running 1unit_test in0hours 0minutes and 0.75seconds (0.75s).16:09:13 16:09:13 Completed successfully16:09:13 16:09:13 Done. PASS=1WARN=0ERROR=0SKIP=0TOTAL=1`Your model is now ready for production! Adding this unit test helped catch an issue with the SQL logic *before*you materialized `dim_customers`in your warehouse and will better ensure the reliability of this model in the future. 

Unit testing incremental models​
--------------------------------

When configuring your unit test, you can override the output of macros, vars, or environment variables. This enables you to unit test your incremental models in "full refresh" and "incremental" modes. 

When testing an incremental model, the expected output is the **result of the materialization**(what will be merged/inserted), not the resulting model itself (what the final table will look like after the merge/insert).



Documentation Source:
docs.getdbt.com/reference/resource-properties/unit-tests.md

Documentation Title:
About unit tests property | dbt Developer Hub

Documentation Content:
comgmail.comexpect:# the expected output given the inputs aboveformat:csvfixture:valid_email_address_fixture_output``unit_tests:-name:test_is_valid_email_address # this is the unique name of the testmodel:dim_customers # name of the model I'm unit testinggiven:# the mock data for your inputs-input:ref('stg_customers')rows:-{email:cool@example.com,email_top_level_domain:example.com}-{email:cool@unknown.com,email_top_level_domain:unknown.com}-{email:badgmail.com,email_top_level_domain:gmail.com}-{email:missingdot@gmailcom,email_top_level_domain:gmail.com}-input:ref('top_level_email_domains')format:sqlrows:|select 'example.com' as tld union allselect 'gmail.com' as tldexpect:# the expected output given the inputs aboveformat:sqlfixture:valid_email_address_fixture_output`0Edit this pageLast updatedon May 16, 2024PreviouswhereNextInputBefore you beginExamples
Edit this pageTerms of ServicePrivacy PolicySecurityCookie Settings© 2024 dbt Labs, Inc. All Rights Reserved.



Documentation Source:
docs.getdbt.com/docs/build/unit-tests.md

Documentation Title:
Unit tests | dbt Developer Hub

Documentation Content:
When to run unit tests​

dbt Labs strongly recommends only running unit tests in development or CI environments. Since the inputs of the unit tests are static, there's no need to use additional compute cycles running them in production. Use them in development for a test-driven approach and CI to ensure changes don't break them. 

Use the resource typeflag `--exclude-resource-type`or the `DBT_EXCLUDE_RESOURCE_TYPE`environment variable to exclude unit tests from your production builds and save compute. 

Unit testing a model​
---------------------

This example creates a new `dim_customers`model with a field `is_valid_email_address`that calculates whether or not the customer’s email is valid: 

`withcustomers as(select*from{{ ref('stg_customers')}}),accepted_email_domains as(select*from{{ ref('top_level_email_domains')}}),check_valid_emails as(selectcustomers.customer_id,customers.first_name,customers.last_name,customers.email,coalesce(regexp_like(customers.email,'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$')=trueandaccepted_email_domains.tld isnotnull,false)asis_valid_email_addressfromcustomersleftjoinaccepted_email_domainsoncustomers.email_top_level_domain =lower(accepted_email_domains.tld))select*fromcheck_valid_emails`The logic posed in this example can be challenging to validate. You can add a unit test to this model to ensure the `is_valid_email_address`logic captures all known edge cases: emails without `.`, emails without `@`, and emails from invalid domains.

`unit_tests:-name:test_is_valid_email_addressdescription:"Check my is_valid_email_address logic captures all known edge cases - emails without ., emails without @, and emails from invalid domains.



