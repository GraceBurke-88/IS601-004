<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - Tracker App</td></tr>
<tr><td> <em>Student: </em> Grace Burke (gnb5)</td></tr>
<<<<<<< Updated upstream
<tr><td> <em>Generated: </em> 2/20/2023 10:10:39 PM</td></tr>
=======
<tr><td> <em>Generated: </em> 2/20/2023 10:19:39 PM</td></tr>
>>>>>>> Stashed changes
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-1-tracker-app/grade/gnb5" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout dev branch and pull any pending changes&nbsp;</li><ol><li>&nbsp;git checkout dev</li><li>&nbsp;git pull origin dev</li></ol><li>Create a new branch for this assignment (see Desired Branch Name)</li><ol><li>git checkout -b MP1-Tracker</li></ol><li>Create a new folder called MP1 in your local repository</li><li>Create a new file called tracker.py</li><li>Copy/paste the content from this template:&nbsp;&nbsp;<a href="https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da">https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da</a></li><li>Add/commit/push the template file</li><ol><li>git add --all</li><li>git commit -m "adding template"</li><li>git push origin MP1-Tracker</li></ol><li>Create a pull request from MP1-Tracker to dev (keep it open, do not close it until you're done)</li><li>Solve the various todo items (also noted below in the deliverables) and fill in the evidence</li><ol><li>Periodically add/commit; recommended after each solved item or every few items</li></ol><li>Save and copy/download the markdown</li><li>Create a new file mp1-submission.md in the MP1 folder</li><li>Add the markdown content</li><li>add/commit/push all the pending files for this assignment (tracker.py and mp1-submission.md)</li><li>If everything looks good on the pull request complete the merge</li><li>Create a new pull request from dev to prod and merge it to update prod (not used yet but you want to keep this up to date)</li><li>checkout dev locally and pull the changes to be up to date</li><li>Navigate to the prod branch on github and find the mp1-submission.md file and get the link to the file to submit to canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Add Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited add_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/220201105-825e444d-41e7-4c26-b42d-97460c14ee78.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sub-Task 1: Add screenshot(s) of the edited add_task() function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/220204554-5d5615e2-0207-40ac-aeb1-cab57bca0714.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>add task<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/220238763-f3f58a49-136e-48e6-96cc-ffe10afcd37f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>comments<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of add_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/220201799-0203f732-c54e-4c6b-ae2d-df2a78344687.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sub-Task 2: Add screenshot(s) showing the success of add_task()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for add_task()</td></tr>
<tr><td> <em>Response:</em> <div><b>#1) update lastActivity with the current datetime value:</b></div><div>I used &nbsp;datetime.now() to get the<br>current date time and then set task["lastActivity"] equal to that.</div><div><br></div><div><b>&nbsp;#2) set the name,<br>description, and due date (all must be provided):</b></div><div>If all of the variables were<br>provided (checked using an if/else statement) I set all the variables in the<br>task item equal to the inputs. (ex:&nbsp;task["name"] = name) which added in new<br>key value pairs.</div><div><br></div><div><b>&nbsp;#3)<span class="Apple-tab-span" style="white-space:pre">	</span>due date must match one of the formats mentioned<br>in str_to_datetime():</b></div><div>I used a try/except statement to see if the input format matched<br>the str_to_datetime(INPUT).</div><div>( &nbsp; try: tests the code for errors (tests if due date<br>mateches str_to_datetime(due) format,&nbsp;</div><div>&nbsp; &nbsp; except: handles the error - prompts for a new<br>input that has the correct format,&nbsp;</div><div>&nbsp; &nbsp; and else: append the task to<br>the list if the formatting is correct.)</div><div><br></div><div><b>&nbsp;#4)&nbsp;add the new task to the tasks<br>list:</b></div><div>If the due date matched then I added the task to the list.</div><div><br></div><div><b>&nbsp;#5)&nbsp;output<br>a message confirming the new task was added or if the addition was<br>rejected due to missing data:</b></div><div>Example of output: "Task added successfully: Name - Wash<br>Dishes, Description - Clean plates and dry them, Due - 12/06/01 12:32:23". In<br>the screen shot I show adding a task with inputs for name/description/due date.<br></div><div><br></div><div><b>&nbsp;#6)<br>&nbsp;make sure save() is still called last in this function:</b></div><div>Called save() at the<br>end of the code block</div><div><br></div><div><b>&nbsp;#7)&nbsp;include your ucid and date as a comment of<br>when you implemented this, briefly summarize the solution:</b></div><div>(see code)</div><div>" gnb5 implemented on 2/18/23</div><div>&nbsp;<br>&nbsp; -------------------</div><div>&nbsp; &nbsp; First I had to update the 'lastActivity' to have the<br>current datatime value.&nbsp;</div><div>&nbsp; &nbsp; I used a print statement to make sure the<br>datetime...."</div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Process Update Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited process_update() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/220206976-737637b8-90d3-4149-ac79-a5bed18d30e1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for edited process_update() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain the solutions to the checklist items for process_update()</td></tr>
<tr><td> <em>Response:</em> <div>&nbsp; &nbsp; 1. For the index passed through, found the task item in<br>the list at that index</div><div>&nbsp; &nbsp; 2. If out of bounds (less index<br>of 0 or greater than the length of the list) prints error message/<br>returns&nbsp;</div><div>&nbsp; &nbsp; 3. Replaced TODO w/current value of each key which was found<br>for the current task</div><div>&nbsp; &nbsp; 4. Passed index, name, description, and due parameters<br>to the update_task function</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Update Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited update_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/220209909-7177b1c7-6d1a-44b1-ab1f-82c1b1e610df.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sub-Task 1: Add screenshot(s) of the edited update_task() function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/220238989-d43aff3b-2b0b-4ca1-adf6-7deaf6d07cae.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>comment<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of update_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/220211891-f43d8d79-86be-4560-aa17-51c6c66fe959.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output of update_task: success<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/220212019-d97ce2f9-0837-40d0-ba20-040bd5f2d524.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output of update_task: failure (no changes)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for update_task()</td></tr>
<tr><td> <em>Response:</em> <div><b>#1 find the task by index</b><br></div><div>&nbsp; &nbsp; --&gt; for the index passed through,<br>found the task item in the list at that index</div><div><b>#2<span class="Apple-tab-span" style="white-space:pre">	</span>consider index<br>out-of-bounds scenarios and include an appropriate message(s) for invalid index</b></div><div>&nbsp; &nbsp; --&gt; if<br>out of bounds (less index of 0 or greater than the length of<br>the list) prints error message/ returns&nbsp;</div><div><b>#3<span class="Apple-tab-span" style="white-space:pre">	</span>update incoming task data if it's<br>provided (if it's not provided use the original task property value)</b></div><div>&nbsp; &nbsp; https://www.sololearn.com/Discuss/1582033/how-to-check-if-input-is-empty-in-python</div><div>&nbsp;<br>&nbsp; --&gt; If provided (use if statements and 'true' if that variable is<br>provided) then set the original task property value to the new value</div><div><b>#4<span class="Apple-tab-span"<br>style="white-space:pre">	</span>update lastActivity with the current datetime value</b></div><div>&nbsp; &nbsp; --&gt; use datetime.now() module and<br>set it equal to the last activity at the current task index</div><div><b>#5<span class="Apple-tab-span"<br>style="white-space:pre">	</span>output that the task was updated if any items were changed, otherwise mention<br>task was not updated</b></div><div>&nbsp; &nbsp; --&gt; Used an if/else statement, I have a<br>variable set before any changes were made to save a local copy of<br>the original task. If the original task has changed prints that items were<br>changed, else prints there were no changes.</div><div><b>#6<span class="Apple-tab-span" style="white-space:pre">	</span>make sure save() is still<br>called last in this function</b></div><div>&nbsp; &nbsp; --&gt; call save() at the end</div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Mark Task Done/Complete Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited mark_done() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/220219845-cdc5442f-a596-4809-97b8-6f4803dee20b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sub-Task 1: Add screenshot(s) of the edited mark_done() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of mark_done()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/220221150-e15eb395-1f08-4431-a86c-096779e6fc2b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success shows something related to the task being marked done/complete<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/220221182-684dc2ec-c388-4111-89cf-1ace0d5e7cd7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure shows something related to the task already being done/complete<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for mark_done()</td></tr>
<tr><td> <em>Response:</em> <div><b>#1 find the task by index</b><br></div><div>&nbsp; &nbsp; --&gt; for the index passed through,<br>found the task item in the list at that index</div><div><b>&nbsp;#2<span class="Apple-tab-span" style="white-space: pre;">	</span>consider<br>index out-of-bounds scenarios and include an appropriate message(s) for invalid index</b></div><div>&nbsp; &nbsp; --&gt;<br>if out of bounds (less index of 0 or greater than the length<br>of the list) prints error message/ returns&nbsp;</div><div><b>&nbsp;#3<span class="Apple-tab-span" style="white-space: pre;">	</span>if it's not done,<br>record the current datetime as the value</b></div><div>&nbsp; &nbsp; --&gt; set 'done' property value<br>to current datetime (using datetime.now()). Also, update lastActivity to the current time. Last,<br>printed out a message that the task was completed.</div><div><b>&nbsp;#4<span class="Apple-tab-span" style="white-space: pre;">	</span>If it<br>is done, print a message saying it's already completed</b></div><div>&nbsp; &nbsp; --&gt; &nbsp;Update lastActivity<br>to the current time (used datetime.now()), and use print to display a message<br>that it's already done.</div><div><b>#5<span class="Apple-tab-span" style="white-space: pre;">	</span>make sure save() is still called last<br>in this function</b></div><div>&nbsp; &nbsp; --&gt; call save() at the end</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> View Task Logic (and list) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited view_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/220221400-863cad17-e37c-4e09-96a4-a67a595aaf41.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sub-Task 1: Add screenshot(s) of the edited view_task() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of view_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/220221524-e65dd276-a45c-44f0-ab5a-e62821f1b2ae.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success shows the task info (given: check list, task name, task description, last<br>activity, due, and completed)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/220221644-9bfe5a1c-56b8-4e3c-b1a6-6a6b0fd8a48e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure shows a related message about task not found or invalid task number<br>or similar<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot(s) of list_tasks() output showing a few examples</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/220221897-b767b244-d763-4dec-95e8-2f846ad47428.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sub-Task 3: Add screenshot(s) of list_tasks() output showing a few examples<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited delete_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/220224942-88f7cee9-961e-4b24-8875-9a6dae31c6b2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sub-Task 1: Add screenshot(s) of the edited get_incomplete_tasks() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of delete_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/220224833-e4416a7d-805b-4ce3-8eda-63c9492f356f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sub-Task 2: Add screenshot(s) showing the success of get_incomplete_tasks()<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/220224892-3400e384-3996-45a1-8352-f65e9e1ebf23.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sub-Task 2: Add screenshot(s) showing the failure of get_incomplete_tasks()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for delete_task()</td></tr>
<tr><td> <em>Response:</em> <div><b>#1 find the task by index</b><br></div><div>&nbsp; &nbsp; --&gt; for the index passed through,<br>found the task item in the list at that index</div><div><b>#2<span class="Apple-tab-span" style="white-space: pre;">	</span>consider<br>index out-of-bounds scenarios and include an appropriate message(s) for invalid index</b></div><div>&nbsp; &nbsp; --&gt;<br>if out of bounds (less index of 0 or greater than the length<br>of the list) prints error message/ returns&nbsp;</div><div><b>#3<span class="Apple-tab-span" style="white-space: pre;">	</span>delete/remove the task from<br>the list by index</b></div><div>&nbsp; &nbsp; source: https://www.programiz.com/python-programming/del</div><div>&nbsp; &nbsp; --&gt; use 'del' to delete<br>items at a given index</div><div>&nbsp; &nbsp;&nbsp;</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Get Incomplete Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_incomplete_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/220225486-ae5d5c12-cb37-4522-8af2-ee363c589228.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sub-Task 1: Add screenshot(s) of the edited get_incomplete_tasks() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_incomplete_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/220225635-9a3c3d0d-7836-4cc8-a467-f2238ec470b4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sub-Task 2: Add screenshot(s) showing the success of get_incomplete_tasks()<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/220225749-3cfd44e8-dd21-4ea9-8794-14de31607144.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sub-Task 2: Add screenshot(s) showing the failure of get_incomplete_tasks()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_incomplete_tasks()</td></tr>
<tr><td> <em>Response:</em> <div><b>#1 generate a list of tasks where the task is not done</b><br></div><div>&nbsp; &nbsp;<br>--&gt; Used a for loop to get tasks that are not done (aka<br>'false'), used .append to add them to the list</div><div><b>#2 pass that list into<br>list_tasks()</b></div><div>&nbsp; &nbsp; --&gt; code already provided</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Get Over Due Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_overdue_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/220229467-cfbf2bba-86cb-4109-9df0-8b87791183bd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sub-Task 1: Add screenshot(s) of the edited get_overdue_tasks() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_overdue_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/220229538-8ebe0c22-4e37-42e3-83f4-730c57b7f1c0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sub-Task 2: Add screenshot(s) showing the success of get_overdue_tasks()<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/220229796-1975f9b4-7525-4f8c-b66a-1e076d9d577b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sub-Task 2: Add screenshot(s) showing the failure of get_overdue_tasks()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_overdue_tasks()</td></tr>
<tr><td> <em>Response:</em> <div><b>#1 generate a list of tasks where the due date is older than<br>now and that are not complete</b></div><div>&nbsp; &nbsp; --&gt; Used a for loop to<br>get tasks that are not done (aka 'false') and have a due date<br>property</div><div>&nbsp; &nbsp; &nbsp; &nbsp; covert the due date to datetime format using the<br>provided function</div><div>&nbsp; &nbsp; &nbsp; &nbsp; used comparison operator to find overdue times and<br>used .append to add them to the list</div><div><b>#2 pass that list into list_tasks()</b></div><div>&nbsp;<br>&nbsp; --&gt; code already provided</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Get Time Remaining Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_time_remaining() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/220232943-364a49d3-c67e-4cbb-bc4b-87057cccfe50.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sub-Task 1: Add screenshot(s) of the edited get_time_remaining() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_time_remaining()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/220233111-1c57da49-5335-490e-8659-462b1c21f8cd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success shows how many days, hours, minutes, seconds until due<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/220233053-420ed7b0-294b-4bcb-af0a-16e17370f5c9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure shows that it&#39;s over due by days, hours, minutes, seconds<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_time_remaining()</td></tr>
<tr><td> <em>Response:</em> <div><b>#1 find the task by index</b></div><div>&nbsp; &nbsp; --&gt; for the index passed through,<br>found the task item in the list at that index</div><div><b>#2<span class="Apple-tab-span" style="white-space: pre;">	</span>consider<br>index out-of-bounds scenarios and include an appropriate message(s) for invalid index</b></div><div>&nbsp; &nbsp; --&gt;<br>if out of bounds (less index of 0 or greater than the length<br>of the list) prints error message/ returns&nbsp;</div><div><b>#3 get the days, hours, minutes, seconds<br>between the due date and now</b></div><div>&nbsp; &nbsp; --&gt; used subtraction and converted the<br>due date to datetime format using given function</div><div><b>&nbsp;#4 to display the remaining time<br>via print in a clear format showing days, hours, minutes, seconds</b></div><div>&nbsp; &nbsp; --&gt;<br>POSITIVE values show time remaining -&gt; display values for days/hours/min/sec and format by<br>first converting to seconds and then dividing accordingly</div><div><b>#5 if the due date is<br>in the past print out how many days, hours, minutes, seconds the task<br>is overdue (clearly note that it's overdue, values should be positive)</b></div><div>&nbsp; &nbsp; --&gt;<br>NEGATIVE values denote time overdue --&gt; use abs value to keep values positive<br>and same math to get days/hours/mins/sec</div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of program output generated from filling in this deliverable (or close to it)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/220234025-452db86b-96ea-44e7-902b-a8462562bdee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sub-Task 1: Add screenshot(s) of program output generated from filling in this deliverable<br>(or close to it)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) of the saved JSON file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/220236213-6995a953-e4c1-4b62-9fb6-4ff291e5191d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sub-Task 2: Add screenshot(s) of the saved JSON file<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Discuss any issues and how they were overcome or learnings from this project</td></tr>
<tr><td> <em>Response:</em> <p>I have done two other todo lists projects so much of the logic<br>and knowledge from said projects carried over to this one. I still ran<br>into a lot of issues, and most of them were just little syntax<br>things I had to brush up on. For example, I did not know<br>how to check if there was no input from the user but then<br>a quick google search said to use &#39;&nbsp;if name:&#39;. There were a dozen<br>other similar issues that were pretty simple to resolve. Doing the time remaing<br>was also pretty challenging for me but again i found a resource (<a href="https://www.w3resource.com/python-exercises/python-basic-exercise-65.php">https://www.w3resource.com/python-exercises/python-basic-exercise-65.php</a>)<br>that made it easier to work out.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request for this assignment (project branch to dev)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/GraceBurke-88/IS601-004/pull/12">https://github.com/GraceBurke-88/IS601-004/pull/12</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-1-tracker-app/grade/gnb5" target="_blank">Grading</a></td></tr></table>