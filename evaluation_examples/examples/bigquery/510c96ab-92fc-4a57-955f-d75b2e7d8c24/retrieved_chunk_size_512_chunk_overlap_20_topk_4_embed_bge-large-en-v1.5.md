Documentation Source:
cloud.google.com/bigquery/docs/visualize-jupyter.md

Documentation Title:
Visualize BigQuery data in Jupyter notebooks  |  Google Cloud

Documentation Content:
```
Query complete after 0.07s: 100%|██████████| 4/4 [00:00<00:00, 1440.60query/s]
Downloading: 100%|██████████| 41/41 [00:02<00:00, 20.21rows/s]
country_code      country_name    num_regions
0   TR  Turkey         81
1   TH  Thailand       77
2   VN  Vietnam        63
3   JP  Japan          47
4   RO  Romania        42
5   NG  Nigeria        37
6   IN  India          36
7   ID  Indonesia      34
8   CO  Colombia       33
9   MX  Mexico         32
10  BR  Brazil         27
11  EG  Egypt          27
12  UA  Ukraine        27
13  CH  Switzerland    26
14  AR  Argentina      24
15  FR  France         22
16  SE  Sweden         21
17  HU  Hungary        20
18  IT  Italy          20
19  PT  Portugal       20
20  NO  Norway         19
21  FI  Finland        18
22  NZ  New Zealand    17
23  PH  Philippines    17
...

```
**Note:**Your results might differ from what is above as the `google_trends`dataset being queried is refreshed with new data on an ongoing basis.
5. In the next cell (below the output from the previous cell), enter the
following command to run the same query, but this time save the results to
a new pandas DataFrame that's named `regions_by_country`. You provide that
name by using an argument with the `%%bigquery`magic command.



Documentation Source:
cloud.google.com/bigquery/docs/samples/bigquery-query-external-sheets-perm.md

Documentation Title:
Query Sheets with a permanent table  |  BigQuery  |  Google Cloud

Documentation Content:
Wait for the query to complete.
w_states = list(results)
print(
 "There are {} states with names starting with W in the selected range.".format(
 len(w_states)
 )
)`What's next
-----------

To search and filter code samples for other Google Cloud products, see the
 Google Cloud sample browser.
 

Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.

* ### Why Google


	Choosing Google CloudTrust and securityOpen cloudMulticloudGlobal infrastructureCustomers and case studiesAnalyst reportsWhitepapersBlog
* ### Products and pricing


	Google Cloud pricingGoogle Workspace pricingSee all products
* ### Solutions


	Infrastructure modernizationDatabasesApplication modernizationSmart analyticsArtificial IntelligenceSecurityProductivity & work transformationIndustry solutionsDevOps solutionsSmall business solutionsSee all solutions
* ### Resources


	Google Cloud documentationGoogle Cloud quickstartsGoogle Cloud MarketplaceLearn about cloud computingSupportCode samplesCloud Architecture CenterTrainingCertificationsGoogle for DevelopersGoogle Cloud for StartupsSystem statusRelease Notes
* ### Engage


	Contact salesFind a PartnerBecome a PartnerEventsPodcastsDeveloper CenterPress CornerGoogle Cloud on YouTubeGoogle Cloud Tech on YouTubeFollow on XJoin User ResearchWe're hiring. Join Google Cloud!Google Cloud Community

About GooglePrivacySite termsGoogle Cloud termsManage cookiesOur third decade of climate action: join us* Sign up for the Google Cloud newsletterSubscribe
EnglishDeutschEspañol – América LatinaFrançaisIndonesiaItalianoPortuguês – Brasil中文 – 简体日本語한국어



Documentation Source:
cloud.google.com/bigquery/docs/samples/bigquery-query-external-sheets-temp.md

Documentation Title:
Query Sheets with a temporary table  |  BigQuery  |  Google Cloud

Documentation Content:
Wait for the query to complete.
w_states = list(query_job)
print(
 "There are {} states with names starting with W in the selected range.".format(
 len(w_states)
 )
)`What's next
-----------

To search and filter code samples for other Google Cloud products, see the
 Google Cloud sample browser.
 

Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.

* ### Why Google


	Choosing Google CloudTrust and securityOpen cloudMulticloudGlobal infrastructureCustomers and case studiesAnalyst reportsWhitepapersBlog
* ### Products and pricing


	Google Cloud pricingGoogle Workspace pricingSee all products
* ### Solutions


	Infrastructure modernizationDatabasesApplication modernizationSmart analyticsArtificial IntelligenceSecurityProductivity & work transformationIndustry solutionsDevOps solutionsSmall business solutionsSee all solutions
* ### Resources


	Google Cloud documentationGoogle Cloud quickstartsGoogle Cloud MarketplaceLearn about cloud computingSupportCode samplesCloud Architecture CenterTrainingCertificationsGoogle for DevelopersGoogle Cloud for StartupsSystem statusRelease Notes
* ### Engage


	Contact salesFind a PartnerBecome a PartnerEventsPodcastsDeveloper CenterPress CornerGoogle Cloud on YouTubeGoogle Cloud Tech on YouTubeFollow on XJoin User ResearchWe're hiring. Join Google Cloud!Google Cloud Community

About GooglePrivacySite termsGoogle Cloud termsManage cookiesOur third decade of climate action: join us* Sign up for the Google Cloud newsletterSubscribe
EnglishDeutschEspañol – América LatinaFrançaisIndonesiaItalianoPortuguês – Brasil中文 – 简体日本語한국어



Documentation Source:
cloud.google.com/bigquery/docs/merchant-center-best-sellers-schema.md

Documentation Title:
Google Merchant Center Best Sellers table schemas  |  BigQuery  |  Google Cloud

Documentation Content:
|**Column****BigQuery data type****Description****Example data**
|  |
|`brand``STRING` best selling brand. |
| --- |
|`category_id``INTEGER` Google product category ID of the best selling brand. |
|`country_code``STRING` Country in which the best selling brand has been sold. |
|`rank``INTEGER` Rank of the best selling brand (the lower the more sold). |
|`previous_rank``INTEGER` Rank of the best selling brand in the previous period (week or month). |
|`relative_demand``STRING` Product's estimated demand in relation to the product with the highest rank in the same category and country. | very\_high, high, medium, low, very\_low |
|`previous_relative_demand``STRING` Relative demand in the previous period (week or month). | very\_high, high, medium, low, very\_low |
|`relative_demand_change``STRING` Change in demand compared to the previous period (week or month). |

**Note:**To access best sellers data, you must meet the eligibility requirements for market insights.Send feedback
 
 Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-05-13 UTC.

* ### Why Google


	Choosing Google CloudTrust and securityOpen cloudMulticloudGlobal infrastructureCustomers and case studiesAnalyst reportsWhitepapersBlog
* ### Products and pricing


	Google Cloud pricingGoogle Workspace pricingSee all products
* ### Solutions


	Infrastructure modernizationDatabasesApplication modernizationSmart analyticsArtificial IntelligenceSecurityProductivity & work transformationIndustry solutionsDevOps solutionsSmall business solutionsSee all solutions
* ### Resources


	Google Cloud documentationGoogle Cloud quickstartsGoogle Cloud MarketplaceLearn about cloud computingSupportCode samplesCloud Architecture CenterTrainingCertificationsGoogle for DevelopersGoogle Cloud for StartupsSystem statusRelease Notes
* ### Engage



