<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3  Business Management</td></tr>
<tr><td> <em>Student: </em> Grace Burke (gnb5)</td></tr>
<tr><td> <em>Generated: </em> 4/10/2023 10:56:38 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-3-business-management/grade/gnb5" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <div>Initial Preperation:</div><div><ol><li>Create two new dynos/VMs in Heroku:</li><ol><li>is601-ucid-mp3-dev</li><li>is601-ucid-mp3-prod</li></ol><li>Configure the heroku config vars and github secrets similar to how dev/prod were setup</li><li>Create two new secrets for github and set the values per the machine names in step 1</li><ol><li>HEROKU_APP_MP3_DEV</li><li>HEROKU_APP_MP3_PROD</li></ol><li>Duplicate your dev/prod yml files and have it listen to the mp3-dev and mp3-prod branches respectively</li><ol><li>Make sure you refer to the proper app secrets from step 3</li><li>You can merge these into regular dev/prod later but you'll want your final project to deploy over it (overwrite) on the normal dev/prod dynos/VM</li></ol><li>You can add this HW branch to the dev yml to test your deployments prior to the pull request to dev from step 4</li></ol></div><div><br></div><div><br></div><ol><li>checkout dev and pull any latest changes</li><li>Create a branch called mp3-prod and immediately push it</li><li>Create a branch called mp3-dev and immediately push it</li><li>Create a branch called MiniProject-3</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li><b>Immediate add/commit/push to github</b></li><li>Open a pull request to mp3-dev and keep it open until you're done adding the submission file</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li><li>&nbsp;pytest BusinessManagement/test/name_of_test.py -rA</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item and add a related commit message for clarity)<br></li><ol><li>Do not delete any provided comments</li></ol><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 10</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together and reuse the image</li><li>Ensure all screenshots are properly captioned in the deliverable section so it's clear what part you're trying to show</li></ol><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from mp3-dev to mp3-prod and merge it</li><ol><li>If you want to keep original dev/prod up to date you can merge the changes into those, but they will cause a deploy to occur for each so be mindful</li></ol><li>Navigate to the submission file under the BusinessManagement folder from mp3-prod</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>Some files will have "DO NOT EDIT" mentioned, please don't edit these. If there's a doubt about any of them ask.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>If a test case isn't possible to complete, capture the failed test case locally via `pytest BusinessManagement -rA` first, then you can rename the function to `off_original_name`.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div>Note: db.py has been updated to use pymysql instead of mysql-connector-python to aid in easier queries.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>May want to download branch as a zip, then copy/paste the files into your repo (if/when you do, please immediately do a git add/commit to record the baseline items)</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231043881-bf2eb169-0cb0-4559-a848-b9721ee2a0a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>URLdisplaying nav.html<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/230996561-c5c7c9af-e1bb-433e-ae1d-79af66244954.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Relevant URLs added<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/230995886-b99c18b2-e36c-4f9c-8f29-767af4bf7555.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB for IS601_MP3_Companies<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/230995950-b2f6404a-de39-4309-ba43-aa03fe7a9dcf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB for IS601_MP3_Employees<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route (code)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/230999314-218edfc9-a465-42cb-982e-069c00f81931.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code should check if the file is a .csv file otherwise reject with<br>a flash<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/230997645-a5cc055c-46f3-4784-bee3-d8260cfe698e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>CSV file should be read from the provided stream as a dict<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/230997872-2cf1e3e1-8d36-490a-b213-c85a3673984b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Extracted company data should be appended as a dict to the company list<br>(only consider data if all fields are present for company/employee)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/230998023-ae23fdff-e598-472e-8361-2c6c64f97030.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>(Companies): After each query a flash message should be generated noting how many<br>records were processed/ if a particular list was empty a flash message should<br>note that the particular list wasn&#39;t loaded or was empty<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/230998137-bb2c006f-057f-4d46-808c-20b32fd4e609.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>(Employees): After each query a flash message should be generated noting how many<br>records were processed/ if a particular list was empty a flash message should<br>note that the particular list wasn&#39;t loaded or was empty<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/230997387-52e18a31-2f5d-4b9d-8df4-c86f1ef5e35c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code should check if the file is a .csv file, prints message showing<br>number of additions<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/230996987-ffb2a093-3e7c-456f-b674-e4de32a7c1c6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Rejects non CSV with a flash<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/230999745-4291507d-a9a8-4d45-85e6-5cf7b050bfc5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company table shows added data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/230995950-b2f6404a-de39-4309-ba43-aa03fe7a9dcf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Employee table shows added data<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231000989-29fa33bb-4447-4efb-a520-fe91c1e66e77.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code should retrieve first_name, last_name, company (id), email<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231000863-a04f4475-2e87-428e-99fc-a0b74307c965.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>first_name is required (flash proper error message if missing), last_name is required (flash<br>proper error message if missing), company doesn&#39;t require a flash and may be<br>empty/None, email is required (flash proper error message if missing)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231000863-a04f4475-2e87-428e-99fc-a0b74307c965.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email format should be verified (regex), also imported at top (import re)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231000705-858c805e-2b08-42ba-8940-7274ed7e63ea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Proper INSERT query should be visible along with the data being passed in<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231000705-858c805e-2b08-42ba-8940-7274ed7e63ea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Except block should have a user-friendly message flashed and a print() of the<br>exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231023267-71818157-47b1-4537-8f50-b514f63fa129.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show filled in valid data prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231023421-a730327e-7b69-4fb9-9036-d28d75f84f0f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231023518-56117d41-24df-45bf-857e-27e3e7a94044.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show first_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231023583-099f53ba-9a5f-4e54-8019-89de08000c8b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show last_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231023652-d2ffb3bc-fed9-4f25-b8d9-d17d7cad73d0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show email error message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231023990-bf4107ec-1f3b-4ee0-b54d-3ae21e948823.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows new employee &#39;Meg Burke&#39;<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231029009-af723a68-a394-494a-88c7-792dfb50bd96.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>SELECT query should be filled in properly to pull employ id, first_name, last_name,<br>email, company_id, company_name via a LEFT JOIN<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231029148-bb16cfef-b7c4-4e60-bb3e-9a2d5c118818.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Check request args for fn, ln, email, company, column, order, limit (exact naming<br>is required)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231029177-3384a862-dbd0-4514-899e-f99bade15caf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>append like filter for first_name/last_name/email/company if provided; should have proper wildcards<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231029297-7fe48600-fa02-44f2-bce3-ba624b808362.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>append sorting if column and order are provided and within the allowed columns<br>and order options (asc, desc) allowed_columns = [&quot;first_name&quot;, &quot;last_name&quot;, &quot;email&quot;, &quot;company_name&quot;]<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231029331-8cd8fc4d-e469-4574-951b-4f495ba6019d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Append limit (default 10) or limit greater than or equal to 1 and<br>less than or equal to 100. Provide a proper error message if limit<br>isn&#39;t a number or if it&#39;s out of bounds<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231029377-da083173-b3c4-4f2f-aa56-d1fc9ae975eb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Except block should have a user friendly message flashed and a print() of<br>the exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231029504-c6174e74-875d-4fa0-b8f8-9e8dcdf3bac3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with first_name filter applied; don&#39;t combine filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231029544-588f517f-3f0c-4a92-9c7e-54e371b57fe4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with last_name filter applied; don&#39;t combine filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231029623-a8b6e242-239e-43f3-b970-dbf4e9383a7d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with email filter applied; don&#39;t combine filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231029705-a6f4d45c-79a6-45b4-9965-fd994b9d42a5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with company filter applied; don&#39;t combine filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231029770-12e14aae-1b1d-4aa2-8adf-e1975ebea543.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show one asc filter applied (clearly label which column was chosen)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231029754-59d8ca87-fa08-41a5-b8a7-8fc283442a0f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show one desc filter applied (clearly label which column was chosen)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231000208-97250bf8-e0cb-45b3-9fb5-73191c70dcf6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code should retrieve first_name, last_name, company (id), email:<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231000333-c24cc770-faff-4dc9-9620-d590daadc4c2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Flashes for missing data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231012772-8a640e1a-9bff-48bb-bfef-b4648c603533.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Proper UPDATE query should be visible/ Proper SELECT query should be visible/ Except<br>blocks (two) should have a user friendly message flashed and a print() of<br>the exception<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231012824-8257fea4-b3d3-40e1-b96c-c7bd13690fb7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Employee data passed to the render_template()/ Except blocks (two) should have a user<br>friendly message flashed and a print() of the exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231001729-128f739f-7523-4d21-888e-632618343dbd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show data before an edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231001794-b016712a-f08f-4619-8101-6c9f7dc63431.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show data after an edit (shows change in first name --&gt; Minnay)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231002831-55683852-0cdc-4e81-b1ac-0997093a75f8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Original employee 888<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231002995-e8e4cf1b-929e-4381-8fd7-e7b1138d1449.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Updated employee 888<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231024516-7fe291a2-d9d2-422b-9a54-e6cd5f173055.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code should retrieve form data for name, address, city, state, country, zip, website<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231024832-24ea0e54-e903-45c2-8f99-08f6b8aa5afa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows requirement for name, address, city, state. Flashes &quot;FEATURE is required&quot; as needed.<br>Tried to implement the pycountry validation but I could not get it to<br>work properly.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231025115-3c65420f-8429-4890-9d98-a316e79c655a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows requirement for country, website, and zipcode. Still allows the change to go<br>through even if website is not included. Flashes &quot;FEATURE is required&quot; as needed.<br>Tried to implement the pycountry validation but I could not get it to<br>work properly.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231025245-174ba31f-154f-4ec7-863e-65388d46252b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Proper INSERT query should be visible along with the data being inserted. Except<br>block should have a user-friendly message flashed and a print() of the exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231013269-bc362dea-60dc-4326-9b2f-151722f1df39.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show filled in valid data prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231013360-d552f758-0409-4aa9-bb38-7f881fe2fd20.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231013601-68ac5526-ff31-42fe-befe-bcfda15f2bda.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231013663-eb6e2d89-d4fa-4ed1-b9e4-0033825dc043.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show address error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231013731-fe7efde9-75de-4321-9eb1-7e5cfdbed2f4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show city error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231013848-3ee5dbc7-9d29-42c0-8edd-f990dc460bd3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show state error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231013896-073a67e3-89e6-4fb6-a381-82800cafc08d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show country error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231013998-78dca28a-28ab-49f0-b411-1a027282bdb4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows zip error message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231014604-17849d77-7989-4f72-83d6-c0a242f0a769.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Includes the valid company data shown previously<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231032977-1c5980c9-8006-4513-a6bd-5d827274404a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>SELECT query should fetch id, name, address, city, country, state, zip, website, employee<br>count (as employee) for the company (likely a sub-query is needed)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231033026-35ab66e9-10d9-4737-a605-6d70b049853d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Check request args for name, country, state, column, order, limit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231033085-0c5eaa51-0cbe-4c8e-80b4-ed1c8034ef53.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>append a LIKE filter for name if provided; should have proper wildcards, append<br>an equality filter for country if provided, 1	append an equality filter for state<br>if provided<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231033140-4b0befdb-fc02-4b54-a714-901c7beac4e7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>append sorting if column and order are provided and within the allows columsn<br>and allowed order asc,desc allowed_columns = [&quot;name&quot;, &quot;city&quot;, &quot;country&quot;, &quot;state&quot;]<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231033202-da542a86-ad9d-43e0-861d-f0a28b0eee9f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>append limit (default 10) or limit greater than or equal to 1 and<br>less than or equal to 100 (continues in screenshot below), provide a proper<br>error message if limit isn&#39;t a number or if it&#39;s out of bounds<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231033292-16407043-9664-4870-9d00-32c68da5e6b6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Except block should have a user friendly message flashed and a print() of<br>the exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231034225-e0a49adc-8dba-46c7-82dc-25a9c9fcdc1c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with name filter applied; don&#39;t combine filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231034315-cd46975f-fe54-431b-b045-d0751067960d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with country filter applied; don&#39;t combine filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231034382-07f45e09-966e-47af-a6e4-63f14c92d06b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with state filter applied; don&#39;t combine filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231034477-60a7b3a2-43e9-4172-b7d0-fda6d6ec2d61.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show one asc filter applied (clearly label which column was chosen: NAME)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231034507-2985e4c1-85ff-44b0-bea6-0c73b36ce4b8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show one desc filter applied (clearly label which column was chosen:Name)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231026649-34532946-0b4b-4ed0-b797-ad4a1437d201.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code should retrieve id (from request args) name, address, city, state, country, zip,<br>website from form. If id isn&#39;t present flash related error message and redirect<br>to company search.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231026685-102a5a6c-2d8e-43d6-8669-af44d4769d59.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Name, address, city, state, country, and zip are required. Flashes message if they<br>are missing.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231026825-6624ff1a-794b-4293-9ec0-6bb4f3b82202.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Proper UPDATE query should be visible with the passed in data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231026825-6624ff1a-794b-4293-9ec0-6bb4f3b82202.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Except blocks (1/2) should have a user friendly message flashed and a print()<br>of the exception<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231026867-e7ab1bd4-c627-424a-8375-075a1649df13.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Proper SELECT query should be visible with the passed in data. Except blocks<br>(2/2) should have a user friendly message flashed and a print() of the<br>exception. Company data should be passed to the render_template()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231027689-3bba5307-076d-4884-b253-d151bc818768.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show data before an edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231027799-58a54bde-e6ac-471b-9cbc-89fe024079c7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show data after an edit (should be different)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231027988-380afed9-f7e4-47c5-bf95-cdb9d8001b4b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB data before (hi-lighted row)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231028079-a3458f4a-f20b-479d-b7a0-873220e420a7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB data after (hi-lighted row)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231003556-65e2176d-3a1c-4406-937a-07829abc9409.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Coade for delete employee route<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231004063-58055b58-be7c-430d-ba18-356508d25b7a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before delete (search page)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231004105-faa6e30f-280e-4b01-b0df-7d248dba4ab7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After delete (search page)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231003627-51a46517-9a1a-4a5c-a51f-1ba602453511.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for delete company route<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231003972-a27a529b-f0a6-46e9-9f50-dd2447e2998c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before deleting company (search page)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231004018-a75f53b0-564d-40f3-95df-e93c8b7f09ed.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After deleting company (search page)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231031092-7db1678e-e0d5-40bb-a7b1-ddf7e7cd10f3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Cases. 25 are passing while 4 failed. I had some issues with<br>getting the purest to work because I accidentally had a line in main.py<br>commented out so I did not have time tor resolve this.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <p>I found this assignment pretty challenging, even though I have used Python Flask<br>I found some of the database work to be new concepts that I<br>really was not familiar with. I had a lot of different issues but<br>for the most part, ran into quite a few type errors and logic<br>errors. For example, having to make the &#39;allowed_columns_tuples&#39; caused some issues for me<br>with the form where the sorting feature did not work. I realized I<br>was not creating the tuple correctly. I also had a few places where<br>I had the wrong variable names which caused a chain reaction of issues<br>(since a lot of the names were similar across company/employee). I will say<br>using many print statements helped me debug most of the problems I ran<br>into. Ultimately, it was just a bit of a time crunch for me<br>because I did not think this project would take me 20 hours.&nbsp;<div><br></div><div>I also<br>tried but could not get the country validated against pycountry package to work<br>properly.&nbsp;</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-3-business-management/grade/gnb5" target="_blank">Grading</a></td></tr></table>