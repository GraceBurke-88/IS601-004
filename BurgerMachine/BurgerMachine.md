<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 2 - Burgers</td></tr>
<tr><td> <em>Student: </em> Grace Burke (gnb5)</td></tr>
<tr><td> <em>Generated: </em> 3/20/2023 5:27:15 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-2-burgers/grade/gnb5" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb">https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb</a>&nbsp;</li><li>Put them into a subfolder in your repository folder (I called my folder BurgerMachine)</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/226213203-558ef947-7e73-41e7-afc0-393132dde03e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Display output which shows the value in currency format (total costs so far<br>in dollars.cents). <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/226213101-5dfae06a-4ccd-432b-a2cc-8eecf0ae5068.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows the implemented code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/226213513-0d6f6c3d-10b3-456e-8d9f-801142334042.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>edited STAGE.pay to handle formatting of currency<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <p>I first, initialized the cost to the 0.00 format. Then, for each item<br>in the inprogress_burger array, add the cost of that item. For each item,<br>&nbsp;I returned the total cost as a variable. I formatted the currency underSTAGE.pay.<br>I used &#39;expected_formatted = &quot;{:.2f}&quot;.format(expected)&#39; to format the expected cost as two decimals.<br>I also added the same formatting code in hadle_pay so that they matched.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/226135964-ea3918b7-437a-45ca-bd42-b7f38ec3b93f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for out of stock<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/226394297-6163606a-3b8a-4fa9-b2ad-bd3954ae8fe1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Console output for out of stock<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/226135994-f72ae5a1-5dee-43a3-9615-dc336ce20482.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for needs cleaning<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/226398529-41447a03-49e0-4467-b49c-9942193dc95c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>output for needs cleaning<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/226136009-aced41b3-153c-4941-8d17-7d4cce6811ba.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>output for invalid choice<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/226400256-0b1171fe-ae8c-4abf-8010-44a8d5c317fe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>output for invalid choice<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/226449118-98f916d5-f900-42ea-91d4-102119b659b8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Exceeded remaining choices code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/226448945-d5d4e7e4-807b-4198-b686-893ae478f604.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Exceeded remaining choices terminal output<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/226136142-d9ac3b82-28ee-4698-a6c2-e9731bedcb5d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid payment code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/226460075-3fb9012b-8514-463d-91be-ed072644b2dd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid payment output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <p><b>OutOfStockException:</b> For this exception, I first printed a message to show that the<br>current item was out of stock. I used self.currently_selecting.name to show the current<br>stage/category. I used lower so that it fits in the message. I sent<br>another message prompting the user to select another item at that stage.&nbsp;<div><br></div><div><b>NeedsCleaningException: </b>For<br>this exception, I first initialized clean to &#39;false&#39; since calling the exception means<br>the machine would not be clean. Then while the machine is not cleaned,<br>I request the user to input the text &#39;clean&#39;. If they input the<br>wrong text, it outputs &quot;Invalid input. Please type &#39;clean&#39; to clean the machine.&quot;<br>Once the user puts in the correct input, the machine will output &quot;The<br>machine has been cleaned&quot;. It then calls self.clean_machine() which refreshes the machine.</div><div><br></div><div><b>InvalidChoiceException: </b>For<br>this exception, the machine outputs<b> &quot;</b>Sorry, that is an invalid choice for STAGE./n<br>Please choose a different STAGE&quot;. Again,&nbsp;&nbsp;I used self.currently_selecting.name to show the current stage/category.</div><div><br></div><div><br></div><div><b>ExceededRemainingChoicesException:</b><br>First, the if statement determines which stage/category the user was selecting when the<br>exception was raised. If the were selecting a patty, a message is printed<br>that says they exceeded the allowed amount of patties and displays the number<br>they exceeded (MAX_PATTIES). Then it moves them to the next stages --&gt; Toppings.&nbsp;If<br>the were selecting a topping, a message is printed that says they exceeded<br>the allowed amount of toppings and displays the number they exceeded (MAX_TOPPINGS). Then<br>it moves them to the next stage --&gt; Pay.&nbsp;</div><div><br></div><div>I used self.currently_selecting.name to show<br>the current stage/category and&nbsp;self.MAX_PATTIES/self.MAX_TOPPINGS to show the maximum that was exceeded.</div><div><div><br></div></div><div><br></div><div><b>InvalidPaymentException: </b>Prints message:<br>&quot;That is an invalid payment&quot;. Then the user is prompted to pay again.<br></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/226142260-c482c2fc-7a28-4f3f-9c09-87211a4ba97c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 1 - bun must be the first selection (can&#39;t add patties/toppings without<br>a bun choice)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/226142292-44aa79d5-7c2f-49b5-9573-6d0ab5dbd17d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 2 - can only add patties if they&#39;re in stock<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/226142306-222daa32-5c3f-4ff3-bd87-fb8c3fe80ad4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 3 - can only add toppings if they&#39;re in stock<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/226143543-5d308034-2447-41c4-a08c-055c3bb7a849.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 4 - Can add up to 3 patties of any combination<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/226143581-fc3e8917-3ed8-4e79-9d25-37d0fbda12e6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 5 - Can add up to 3 toppings of any combination<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/226143597-977ac08a-30b1-4f67-855d-8f075a3b7ed8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 6 - cost must be calculated properly based on the choices (check<br>for currency format as part of this) (test case should have a few<br>permutations of at least 3 valid burgers)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/226148950-cd4e7472-87df-47e0-b748-c7ee80d57f38.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 7 - Total Sales (sum of costs) must be calculated properly (test<br>case should have a few permutations of at least 3 valid burgers)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/226148965-ebb8a037-7f7b-4ed2-9cae-e151401d637c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 8 - Total burgers should properly increment for each purchase<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/226148994-737e17df-6da3-4762-bb29-ea161418370b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Part 1: Show all Tests 1-8 passing and any relevant output (it should<br>be clear which test case is which) Best to use &#39;pytest -rA&#39; on<br>the command line<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/226149007-23dd8deb-186d-492c-b34c-bb1f98a243d3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Part 2: Show all Tests 1-8 passing and any relevant output (it should<br>be clear which test case is which) Best to use &#39;pytest -rA&#39; on<br>the command line<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/226149013-b9dc732c-5b04-44f5-9144-41b5d2931340.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Part 3: Show all Tests 1-8 passing and any relevant output (it should<br>be clear which test case is which) Best to use &#39;pytest -rA&#39; on<br>the command line<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <p><b>Test 1 - bun must be the first selection (can&#39;t add patties/toppings without<br>a bun choice)-</b>&nbsp;use with pytest.raises(InvalidStageException): to check that an &#39;InvalidStageException&quot; is raised when<br>a patty (machine.handle_patty(&quot;veggie&quot;))/ or topping(machine.handle_toppings(&quot;cheese&quot;)) is added without a bun. I used a<br>print statement just to help me so I know what the test is<br>doing.<div><br></div><div><b>Test 2 - can only add patties if they&#39;re in stock</b>- I first<br>reset the machine so that test 1 does not impact test 2. Then<br>I used assert to check that all the patties were in stock (had<br>a quantity greater than zero). I then selected a bun (machine.handle_bun(&quot;white burger bun&quot;)).<br>Next, I had the machine add a patty that was IN STOCK(machine.handle_patty(&quot;beef&quot;)) as<br>a base test. I then checked that the patty was added and the<br>patty quantity was correct. Next, I wanted to check a patty that was<br>out of stock, so I used up all the beef par=tties. When I<br>tried to add another beef patty, an&nbsp;OutOfStockException was correctly raised.</div><div><br></div><div><b>Test 3 - can<br>only add toppings if they&#39;re in stock-</b>&nbsp;I reset the burger machine using&nbsp;machine.reset(). Then<br>I chose a bun, and a patty, and selected next to move to<br>the toppings stage. Then I set the quantity of &#39;bbq&#39; to 0. I<br>then tried to add the &#39;bbq&#39; topping and made sure it raised an<br>OutOfStockException. Then I checked that another in-stock topping could be added so the<br>flow of the machine was not interrupted.<br></div><div><br></div><div><b>Test 4 - Can add up to<br>3 patties of any combination- </b>I first reset the machine. Then I&nbsp;increment beef<br>patties to 1 (machine.patties[2].quantity = 1). Then I had the machine select a<br>bun. Then I added three patties to the burger. I asserted that the<br>patties were added ex:(assert machine.inprogress_burger[1].name.lower() == &quot;beef&quot;). Then I checked that trying to<br>add a fourth patty raised an&nbsp;ExceededRemainingChoicesException.<br></div><div><br></div><div><b>Test 5 - Can add up to 3<br>toppings of any combination- </b>Again, I first reset the machine. Then I gave<br>&#39;bbq&#39; a quantity of 5 (machine.toppings[7].quantity = 5). Then I selected a bun<br>and said &#39;next&#39; to selecting a patty. I then added three toppings (machine.handle_toppings(&quot;lettuce&quot;),<br>machine.handle_toppings(&quot;tomato&quot;), machine.handle_toppings(&quot;bbq&quot;)). I then checked that these toppings were added ( made sure<br>the length of the in-progress burger was 4). Then I checked that the<br>index of each topping was correct. I then tried to add a fourth<br>topping and checked that it raised an ExceededRemainingChoicesException. I then made sure the<br>toppings were still correct and that a fourth topping was not added.</div><div><br></div><div><b>Test 6<br>- cost must be calculated properly based on the choices (check for currency<br>format as part of this) (test case should have a few permutations of<br>at least 3 valid burgers)</b><br></div><div>I tested three different burger permutations and asserted that<br>the total was correct for each burger. I made sure to reset the<br>machine each time to make sure that it was reset. I used (assert<br>machine.calculate_cost() == 3.5) to make sure the calculated cost was correct. Then I<br>used (machine.handle_pay(3.5, &quot;3.50&quot;)) to pay and make sure I can finalize the transaction.<br>Calculate_cost() checks for the currency format.</div><div><b><br></b></div><div><b>Test 7 - Total Sales (sum of costs)<br>must be calculated properly (test case should have a few permutations of at<br>least 3 valid burgers) </b>I first reset the machine and printed the current<br>total sales which are 0 (print(&quot;The total sales when starting:&quot;, machine.total_sales)). Then I<br>made three different orders and went through calculating the cost and handling the<br>payment and asserted each time that the total cost was correctly incrementing.(assert machine.total_sales<br>== 7.25)<br></div><div><br></div><div><b>Test 8 - Total burgers should properly increment for each purchase-</b> I<br>first reset the machine. I created three different orders and checked each time<br>that the total number of burgers incremented accordingly ex: (assert machine.total_burgers == 1)<br>after the third order (assert machine.total_burgers == 3) and I printed the total<br>(print(&quot;Total burgers:&quot;, machine.total_burgers)).</div><div><br></div><div><br><div><br></div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707795-a9c94a71-7871-4572-bfae-ad636f8f8474.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td>Not provided</td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>(missing)</p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-2-burgers/grade/gnb5" target="_blank">Grading</a></td></tr></table>