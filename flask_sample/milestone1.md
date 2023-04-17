<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Grace Burke (gnb5)</td></tr>
<tr><td> <em>Generated: </em> 4/17/2023 4:57:00 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone1-deliverable/grade/gnb5" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231845623-b8fac73f-91d3-472d-9a9d-4cf2dcf40cdd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show invalid email validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231845795-91df8d4c-33c2-4d4a-a3a6-383d7fe0fa20.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show invalid password validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231845992-01e78527-0610-4837-a495-7451e988f12a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show passwords not much validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231846131-189febf2-ab1f-4da8-b059-3b642ac6e7b9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show email not available validation (already registered)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231846252-bdd39ef0-a88a-445e-96f1-516ec9bb5e21.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show username not available validation (username is taken)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231842479-53f253c4-03c5-4da4-8d28-0363748e4495.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show the form with valid data filled in before the form is submitted<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231843032-0c25326e-d8b0-4c0b-8291-cd2375d0c687.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>ROW 4 / Users Table with data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/GraceBurke-88/IS601-004/pull/39">https://github.com/GraceBurke-88/IS601-004/pull/39</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p><b>How the form is handled and behaves:</b><div>- The register page is available to<br>non-authenticated users</div><div>- the register() function in auth.py renders register.html</div><div>- the registration form includes<br>fields for email, username, password, and password confirmation</div><div>- on submit the user&#39;s input<br>is sent to the server via the POST method</div><div>- register() is triggered which<br>handles the form data</div><div><br></div><div><div><div><b>Validation logic (frontend and backend):</b></div><div><div>- Frontend validation: The RegisterForm automatically<br>generates HTML input elements with appropriate attributes (e.g., &#39;required&#39;, &#39;type=&quot;email&quot;&#39;) for basic client-side<br>validation in the browser.</div><div>- &nbsp;Backend validation: When the form is submitted, the server-side<br>validation checks are triggered by form.validate_on_submit() in the register() function. The user will<br>be presented with relevant error messages if the form fails validation.</div></div><div><br></div><div><b>Password is handled:</b></div><div><div>-<br>The password and password confirmation fields are securely submitted to the server using<br>the POST method in the form.</div><div>- The submitted password is hashed using bcrypt<br>before storing it in the database: bcrypt.generate_password_hash(password). This ensures that the plaintext password<br>is never saved, enhancing security.</div></div><div><b><br></b></div><div><b>DB is utilized:</b><br></div></div><div>- if the input is considered valid<br>and after the password is hashed</div><div>- the new user and related data is<br>inserted into IS601_USERS</div><div><div>- If the insert operation is successful, flashes a success message.<br>If an error occurs, such as a duplicate email or username, a relevant<br>error message will be displayed.</div></div><div><br></div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231846863-97a742e0-dc8d-4c18-8524-831f9771a8b4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show password mismatch validation (doesn&#39;t match what&#39;s in the DB)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231847026-27d23a5b-f794-4518-98a8-39ac33366a94.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show validation based on non-existing user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231847268-5e5c3f54-06ee-4f95-bfe4-447bc8f3fa10.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Should have a flash message and/or a redirect to a landing page (post-login)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/GraceBurke-88/IS601-004/pull/39">https://github.com/GraceBurke-88/IS601-004/pull/39</a> </td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/GraceBurke-88/IS601-004/pull/55">https://github.com/GraceBurke-88/IS601-004/pull/55</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p><b>How the form is handled and behaves:</b><div>- when the user (not logged in)<br>clicks the login page they are prompted to input a email or username<br>and password</div><div>- when the form is submitted a POST method sends it to<br>the server and the login() function in auth.oy hadles the form data</div><div>- if<br>any input is missing a flash message appears&nbsp;</div><div>- then the code authenticates the<br>password associated with username/emai</div><div>- if it matches, the user is logged in and<br>the user is redirected to the login</div><div>- if unsuccessful the appropriate error message<br>flashes</div><div><b style="caret-color: rgb(55, 65, 81); color: rgb(55, 65, 81); white-space: pre-wrap;"><br></b></div><div><b style="caret-color: rgb(55,<br>65, 81); color: rgb(55, 65, 81); white-space: pre-wrap;">Validation logic (frontend and backend):</b></div><div><div>- Frontend<br>validation: The LoginForm automatically generates HTML input elements with appropriate attributes (e.g., &#39;required&#39;,<br>&#39;type=&quot;email&quot;&#39;) for basic client-side validation in the browser.</div><div>- Backend validation: When the form<br>is submitted, the server-side validation checks are triggered by form.validate_on_submit() in the login()<br>function. The user will be presented with relevant error messages if the form<br>fails validation.</div></div><div>- email is validated with validate_email (checks for @)</div><div>- password is checked<br>to be of length 8 and that it matches confirm password (same for<br>confirm pass)</div><div>- username is expected to be between 2-30 characters and to match<br>a particular regular expression pattern&nbsp;</div><div><div><div><b><br></b></div><div><b>Password is handled:<br></b></div><div>The code (auth.py/login) first grabs the hashed<br>password from the DB and provides a boolean as to whether the hashed<br>password from the DB matches the user&#39;s password input (uses bcrypt). If so,<br>the user can log in, otherwise the message &quot;Ivalid Password&quot; flashes.</div><div><b><br></b></div><div><b>DB is utilized:</b><br></div></div><div>The<br>DB record is selected using the matching email/username pair.&nbsp;</div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231847434-415c7a66-e960-42f9-87a5-e06f24e63d4a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Message should show something about being logged out<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/232604819-c1b9be17-87c1-4886-882f-d870fcc26a83.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Message showing logged in user cannot access &#39;profile&#39; page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/GraceBurke-88/IS601-004/pull/44">https://github.com/GraceBurke-88/IS601-004/pull/44</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div><b>Importing session:</b> The session object is imported from the flask module, which provides<br>a simple and secure way to store data for each user.</div><div><br></div><div><b>Storing user information:</b><br>Upon successful login, the user object is converted to JSON format and stored<br>in the session using session["user"] = user.toJson(). This allows the application to remember<br>the user's information across requests, such as their email, username, and roles.</div><div><br></div><div><b>Accessing user<br>information:</b> Once the user information is stored in the session, it can be<br>accessed throughout the application to personalize content and determine access permissions. For example,<br>the current_user object (from Flask-Login) can be used to access the user's data<br>and check if they are authenticated, which is required for accessing certain protected<br>routes.</div><div><br></div><div><b>Logging out: </b>When a user logs out, the logout() function in auth.py clears<br>the user's session data. It removes the Flask-Principal identity keys and sends an<br>identity_changed signal with an AnonymousIdentity. This ensures that the user's information is no<br>longer available in the session and that the user is treated as an<br>anonymous visitor.</div><div><br></div><div><b>Session expiration:</b> Flask sessions have an expiration time, after which the session<br>data is automatically cleared. This helps maintain security by ensuring that user data<br>is not stored indefinitely on the server. The expiration time can be configured<br>in the Flask application settings.</div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/232604819-c1b9be17-87c1-4886-882f-d870fcc26a83.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>(same as previous)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/232601353-7e1c00c1-64d6-46f2-8678-496d011f00f2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Trying to access roles/add without being logged in to an admin account<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/232348965-0d7aca17-ff1b-41b4-8eeb-135484b08e1c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Roles table with Admin/Reviewer/Publisher<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/232349039-58ccf8a8-24f1-4239-a603-edd24b5b3776.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>UserRoles Table<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/232349051-844e3398-de5c-4318-aa40-4b2b657954ae.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Users tables showing User #1 who has admin status<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/GraceBurke-88/IS601-004/pull/44">https://github.com/GraceBurke-88/IS601-004/pull/44</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>The code uses the flask_login module to help manage user sessions and protect<br>pages that require a user to be logged in.<br><div><div>- A login_manager is set<br>up to work with the app and help manage user sessions.</div><div>- The load_user<br>function is created to get user information from either the session (a temporary<br>storage- jsons.loads method) or the database.</div><div>- The identity_loaded signal connects to a function<br>that sets up user information related to authentication and permissions (what they can<br>access).</div><div>- To protect a page or view, the @login_required decorator is added before<br>its definition in the code. This means that only logged-in users can access<br>that page.</div></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <div>- Import flask_principal to manage user roles and protect pages.<br></div><div>- Create a Principal<br>object and connect it to the Flask app.</div><div>- Link the identity_loaded signal to<br>a function that updates the user's authentication and roles.</div><div>- Store and retrieve user<br>roles from the database and add them to the user's identity.</div><div>- Use the<br>Permission class and RoleNeed to protect pages based on roles. For example, limit<br>access to an "admin" route only to users with the "admin" role.</div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/232340693-08e39876-3576-43f1-88ee-f4883ee0e933.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>UI- Navigation should be styled<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/232340705-650cf140-a056-4b78-8a5f-57bd985cd512.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>UI- UI shouldn&#39;t have any odd artifacts that are unstyled<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/232340721-1b03bdeb-a42f-43fe-9f2b-e2d3eab9be84.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>UI- 	Forms should be styled<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/232340727-e4083e35-0022-406c-8a2d-4fa8489d8652.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>UI- 	Forms should be styled<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/232340741-dbca5201-6ee2-4c0f-a0a4-7844e248bacb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>UI- Data output should be in a clean manner (i.e., table, row/cols, list<br>groups, etc) Basically not exactly like dumped plaintext<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/GraceBurke-88/IS601-004/pull/36">https://github.com/GraceBurke-88/IS601-004/pull/36</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p>Basic styling is all provided by the Bootstrap library. The library has different<br>UI components available and a prebuilt library of colors to use for different<br>features. It also provides built-in responsiveness, which is a huge time saver. The<br>navbar is simple with different links for the different pages. The forms are<br>also simple with bootstrap-provided field areas and buttons.&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231846863-97a742e0-dc8d-4c18-8524-831f9771a8b4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid password on login<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231846252-bdd39ef0-a88a-445e-96f1-516ec9bb5e21.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Username not available on registration <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/231846863-97a742e0-dc8d-4c18-8524-831f9771a8b4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid password on login<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/GraceBurke-88/IS601-004/pull/36">https://github.com/GraceBurke-88/IS601-004/pull/36</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <ul><br><li>The Flask flash() function is used to display user-friendly messages, such as<br>success, warning, or error messages, to inform users about the result of their<br>actions. The messages are categorized using different Boostrap CSS classes (e.g., &quot;success&quot;, &quot;warning&quot;,<br>&quot;danger&quot;) to visually indicate their nature.<div><div>- Custom error handling: Using custom error handling<br>to provide more relevant information to users (for example check_duplicate() checks if a<br>username has already been used and lets the user know if that is<br>the case)</div><div><br></div></div><br></li><br></ul><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/232340721-1b03bdeb-a42f-43fe-9f2b-e2d3eab9be84.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email and username should prefill <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/GraceBurke-88/IS601-004/pull/45">https://github.com/GraceBurke-88/IS601-004/pull/45</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <div><div>- Found in: profile() function in auth.py<br></div></div><div><div>- Get the logged-in user's ID using<br>current_user.get_id().</div><div>- Create a form using the ProfileForm class.</div><div><div>- A try-except block is used<br>to retrieve the user's data from the database by executing a SELECT query<br>with the user ID as a parameter (SELECT id, email, username FROM IS601_Users<br>where id = %s). The result is stored in the result variable.</div></div><div>- If<br>the query is successful, create a user object with the retrieved data.</div><div>- Load<br>the user's username and email into the form.</div><div>- Display the form with user<br>data on the profile page by rendering the profile.html template.</div></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/232341693-744fb2d7-db03-49a5-a314-fe4ca46d2d7c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show username validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/232341742-511eee10-c1e6-441c-8ff0-843897afb111.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show email validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/232341774-05d9105d-4fb6-4ea0-ac8d-1d3a3ac897a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show password validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/232341815-3e961d34-fd42-43c4-8788-6a7969cbf83e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show password mismatch message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/232341877-9a0a6d0a-e48f-4854-872d-a42bd90b60ec.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show username already in use message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/232341848-7506bfce-e19b-4b9e-aedc-14d0aa5faefc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show email already in use message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/232341159-6663a160-3de3-462c-90b8-f79741cc5904.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB Before<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/232341931-89658e01-dfae-4aa0-bfdf-2f0566ef246e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB after (Record #1)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/GraceBurke-88/IS601-004/pull/45">https://github.com/GraceBurke-88/IS601-004/pull/45</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <div>- When the user submits the form, the updated email, username, and current<br>password are collected from the form.</div><div>- If the user wants to change their<br>password, the code first checks if the current password is correct. If it<br>is, the new password is hashed and updated in the database.</div><div>- The code<br>updates the email and username in the database using a query, including the<br>email, username, and user ID.</div><div>- Before making any changes to the database, the<br>code checks for duplicates or invalid entries to ensure the update is valid.</div><div>-<br>If everything goes well, the user's session information is updated with the new<br>email and username, and a success message is shown.</div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>I had an issue with my DB not updating since I had missed<br>one of the changes in one of the files, professor was able to<br>help me debug and find where the problem was stemming from. I learned<br>a lot more about authentication in class such as using bcrypt for hashing<br>and password validation which is not something I have used in the past.&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td>Not provided</td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone1-deliverable/grade/gnb5" target="_blank">Grading</a></td></tr></table>