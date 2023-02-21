<table><tr><td> <em>Assignment: </em> M2 Python-HW</td></tr>
<tr><td> <em>Student: </em> Grace Burke (gnb5)</td></tr>
<tr><td> <em>Generated: </em> 2/1/2023 8:53:00 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/m2-python-hw/grade/gnb5" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you have the dev/prod branches created before starting this assignment.</p><p>Pre-req Steps if not done so yet:</p><p><ol><li>git checkout main</li><li>git checkout -b dev</li><li>git push origin dev</li><li>git checkout -b prod</li><li>git push origin prod</li></ol><div>This will ensure you have a dev and prod branch on github.</div></p><p>Setup steps:</p><ol><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li><li><code>git checkout -b M2-Python-HW</code></li></ol><p>You'll have 3 problems to save for this assignment.</p><p>Each problem you're given a template&nbsp;<strong>Do not edit anything in the template except where the comments tell you to</strong>.</p><p>The templates are done in such a way to make it easier to capture the output in a screenshot (if it's still not able to fit well, you can zoom out in your browser).</p><p>You'll copy each template into their own separate .py files, immediately git add, git commit these files (you can do it together) so we can capture the difference/changes between the templates and your additions. This part is required for full credit.</p><p>HW steps:</p><ol><li>Open your IDE at the root of your repository folder</li><li>In your IDE create a new folder/directory called M2</li><li>Create 3 new files in this new M2 folder (problem1.py, problem2.py, problem3.py)</li><li>Paste each template into their respective files</li><li><code>git add .</code></li><li><code>git commit -m "adding template baselines</code></li><li>Do the related work (you may do steps 8 and 9 as often as needed or you can do it all at once at the end)</li><li><code>git add .</code></li><li><code>git commit -m "completed hw"</code></li><li>When you're done push the branch<ol><li><code>git push origin M2-Python-HW</code></li></ol></li><li>Create the Pull Request with&nbsp;<strong>dev</strong>&nbsp;as base and&nbsp;<strong>M2-Python-HW</strong>&nbsp;as compare</li><li>Create a new file in the M2 folder in your IDE called m2_submission.md</li><li>Fill out the below deliverable items, save the submission, and copy to markdown<ol><li>For this assignment you may get screenshots from your IDE output or terminal/console output</li></ol></li><li>Paste the markdown into the m2_submission.md</li><li>add/commit/push the md file<ol><li><code>git add m2_submission.md</code></li><li><code>git commit -m "adding submission file"</code></li><li><code>git push origin M2-Python-HW</code></li></ol></li><li>Merge the pull request from step 11</li><li>On your local machine sync the changes<ol><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li></ol></li><li>Make a pull request from&nbsp;<strong>prod</strong>&nbsp;as base and&nbsp;<strong>dev</strong>&nbsp;as compare and immediately merge it</li><li>Submit the link to the m2_submission.md file from the prod branch to Canvas</li></ol><p><strong>Template Files</strong>&nbsp;You can find all 3 template files in this gist:&nbsp;<a href="https://gist.github.com/MattToegel/3c55ca7bb631ff6f492bf6f1ad27270e">https://gist.github.com/MattToegel/3c55ca7bb631ff6f492bf6f1ad27270e</a></p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Problem 1 - Only output Odd values of the Array under "Odds output" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Clearly screenshot the output of Problem 1 showing the data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/216203308-ba1559ca-6970-4e1a-9afb-f034629c7a6f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>problem 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/216203455-e74d7b27-e348-4360-9a8d-8a8dde70e1ba.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>problem 1 output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Describe how you solved the problem</td></tr>
<tr><td> <em>Response:</em> <p>First I created an empty array called &#39;odds&#39;. I used a for loop<br>to iterate through the given arrays. &nbsp;Then I used an if statement with<br>the condition being if the &#39;%&#39; operator was not equal to zero (which<br>would indicate the value not being 0 or a negative value). Then the<br>odd values were appended to the array. Last, the array was printed out.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Problem 2 - Only output the sum/total of the list values by assigning it to the 'total' variable (the number must end in 2 decimal places, if it ends in 1 it must have a 0 at the end) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Clearly screenshot the output of Problem 2 showing the data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/216204155-670f0987-27ad-4805-bec6-91e1a35574bb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Problem 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/216204295-40079587-aaac-4bb9-977f-7f972383b1f8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Problem 2 output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Describe how you solved the problem</td></tr>
<tr><td> <em>Response:</em> <p>I again used a for loop to iterate through the array. For each<br>value in the array, I added that value to the &#39;total&#39; (a predefined<br>variable).&nbsp;<div><br></div><div>To round to two decimal places I added &#39;: .2f&#39; to show the<br>value should print out and round to two decimal places.</div><div><br></div><div>&nbsp;&#39;print(&quot;\nThe total is {:<br>.2f}\n&quot;.format(total))&#39;</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Problem 3 - Output the given values as positive under the "Positive Output" message (the data otherwise shouldn't change) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Clearly screenshot the output of Problem 3 showing the data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/216206477-e5f203e1-52f7-4a2c-9f0e-f70bada0ca0b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Problem 3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/216206511-1d9101ea-9c11-4e2d-8ef6-b329e80964af.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Problem 3 output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Describe how you solved the problem</td></tr>
<tr><td> <em>Response:</em> <p>Create an empty array called &#39;pos&#39;. Iterated through the given arrays using a<br>for loop. To handle the string data type I used an if statement<br>(if a string...) then I changed the type to int, took the absolute<br>value, and then reverted the type back to a string. For all other<br>data types then went to &#39;else&#39; and I simply took the absolute value<br>(worked for floats/ints). Then I appended these values to the &#39;pos&#39; array and<br>printed the array (for each of the given arrays).<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc Items </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Pull Request URL for M2-Python-HW to dev</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/GraceBurke-88/IS601-004/pull/8">https://github.com/GraceBurke-88/IS601-004/pull/8</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Talk about what you learned, any issues you had, how you resolve them</td></tr>
<tr><td> <em>Response:</em> <p>I got a bit of a refresher on Python since I have not<br>worked with the language in a bit. Especially with doing the zybooks assignment<br>there were a lot of little things I had forgotten like the nuiances<br>between dictionaries, arrays, etc. One issue I ran into was how to change<br>the type of a string so that I could change the sign so<br>had to review casting. &nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/m2-python-hw/grade/gnb5" target="_blank">Grading</a></td></tr></table>
