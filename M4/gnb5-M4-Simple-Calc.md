<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Grace Burke (gnb5)</td></tr>
<tr><td> <em>Generated: </em> 2/26/2023 6:11:10 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/m4-simple-calc/grade/gnb5" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you're working in an up to date branch</p><ul><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li><li><code>git checkout -b M4-Simple-Calc</code></li></ul><p>This will likely be started in class.</p><p>Steps:</p><ol><li>Create a new Folder called M4</li><li>Create a new file called MyCalc.py inside this folder</li><li>Create a MyCalc Class</li><li>Define basic addition / subtraction / multiplication / division functions<ol><li>These functions should update an internal variable as a running total/value called&nbsp;<code><b>ans</b></code></li><li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero for example)</li><li>Since you'll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li></ol></li><li>Define a "main" logic to run when the program runs</li><li>This logic should ask for user input<ol><li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol><li>This will do an immediate calculation, print it, and store the answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li><li>Alternatively, the input can be&nbsp;<code>ans</code>, any valid math operator, any valid number (i.e.,&nbsp;<code>ans</code>&nbsp;* 2)<ol><li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li></ol></li><li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass (test cases should have a series of data passed into them)<ol><li>Test number-add-number</li><li>Test ans-add-number</li><li>Test number-sub-number</li><li>Test ans-sum-number</li><li>Test number-mult-number</li><li>Test ans-mult-number</li><li>Test number-div-number</li><li>Test ans-div-number</li></ol></li><li>Create a new file called m4_submission.md inside the M4 folder</li><li>Fill out the below deliverables</li><li>Generate the markdown and paste it into the m4_submission.md</li><li><code>git add .</code></li><li><code>git commit -m "adding m4 hw"</code></li><li><code>git push origin M4-Simple-Calc</code></li><li>Create a pull request M4-Simple-Calc to dev</li><li>Create a pull request dev to prod (after the previous one is merged)</li><li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li><li>Submit this link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/221440311-fea5593c-848c-400f-adca-c5ee705a0764.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows code for addition<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/221440296-c435276d-022d-4910-9efb-54040f66e829.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows console/addition working<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/221440355-62fd0eea-69b2-49bc-bd71-304fee83a064.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows subtraction<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/221440377-10f35afb-128e-4605-a725-1843763aa448.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows console/subtraction working<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/221440401-e0815908-3a3d-4f38-9e25-86388e1992f7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows multiplication<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/221440423-1e78877c-c20f-44ca-a715-0e79476567d2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows console/multiplication working<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/221440436-0207446b-59f5-4120-b434-b4a8c47d2ceb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Multiplication method<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/221440475-c11502f3-ea0d-4411-afe2-54461fc0d941.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows console and division for ints/floats and the divide by zero error handling<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of passing number-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/221440626-8e121cb9-854f-4830-b8c5-633e10dd0140.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows test case and processing a series of data to run the test<br>case over<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/221440682-5990c157-442b-4125-8d88-bdb914de4a91.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case passing in pytest<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of passing ans-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/221441860-cf15e7c4-2cc6-4d94-afaa-e3d3a2738eff.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Processing a series of data to run the and-add-num test case over (the<br>answer of each previous test will be used for the following one)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/221440682-5990c157-442b-4125-8d88-bdb914de4a91.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case passing in pytest<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of passing number-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/221440682-5990c157-442b-4125-8d88-bdb914de4a91.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case passing in pytest<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/221440835-a3ba8014-bbe7-4356-9b4a-b72b9b582461.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Processing a series of data to run the num-sub-num test case over<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshots of passing ans-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/221440682-5990c157-442b-4125-8d88-bdb914de4a91.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case passing in pytest<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/221442142-da723ce8-4a7b-4177-9c64-412257adf853.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Processing a series of data to run the and-sub-num test case over (the<br>answer of each previous test used for the following one)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshots of passing number-mult-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/221440682-5990c157-442b-4125-8d88-bdb914de4a91.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case passing in pytest<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/221440904-7e227117-0aa4-4cd9-889d-29d81e8c4853.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Processing a series of data to run the num-mult-num test case over<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshots of passing ans-multi-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/221440682-5990c157-442b-4125-8d88-bdb914de4a91.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case passing in pytest<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/221442231-9291c69d-03c9-4985-a0f7-5df5dbfd17f0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Processes a series of data to run the ans-mult-num test case over (the<br>answer of each previous test is used for the following one)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshots of passing number-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/221440682-5990c157-442b-4125-8d88-bdb914de4a91.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case passing in pytest<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/221441386-18aa72f5-92f1-4c24-8684-c4795aec8fea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Processing a series of data to run the num-div-num test case over<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshots of passing ans-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/221440682-5990c157-442b-4125-8d88-bdb914de4a91.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case passing in pytest<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/221442350-dd18d1db-e727-4e32-a75d-8dedcbdd30e1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Processes a series of data to run the and-div-num test case over (the<br>answer of each previous test is used for the following one)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <p>During this assignment I learned about adding test cases and how to formulate<br>them. It is pretty straightforward so once I figured the first couple out<br>it was quite easy to create the others. I also got to have<br>more of a hands on experience of dealing with some data types, such<br>as in class when we looked at an error that was causing by<br>incorrectly casting the string input to int/float. I also ran into an issue<br>with this because intially the &nbsp;&#39;__asnumber&#39; method was changing the precision of the<br>float values to ints because of the logics so I had to move<br>the testing for float first.<div><br></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>Test cases (in this project unit tests) are used to check if sigular<br>components are working correctly. Using the test case I simulated potential user input<br>and used assertions to validate the proper output. Though this was a rellatively<br>simple application, I still caught a few errors in working through my test<br>cases (as mentioned above) so I see how tests cases can become crucial<br>to larger projects. I have worked with test cases in Github before but<br>they were already provided by that Professor&#39;s repo so I would be intrested<br>in learning how to implement my own automated test cases for Github.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/GraceBurke-88/IS601-004/pull/16">https://github.com/GraceBurke-88/IS601-004/pull/16</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/m4-simple-calc/grade/gnb5" target="_blank">Grading</a></td></tr></table>
