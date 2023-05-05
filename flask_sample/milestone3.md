<table><tr><td> <em>Assignment: </em> IS601 Milestone 3 Shop Project</td></tr>
<tr><td> <em>Student: </em> Grace Burke (gnb5)</td></tr>
<tr><td> <em>Generated: </em> 5/5/2023 9:59:02 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-3-shop-project/grade/gnb5" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone3 branch</li><li>Create a new markdown file called milestone3.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone3.md</li><li>Add/commit/push the changes to Milestone3</li><li>PR Milestone3 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 4</li><li>Submit the direct link to this new milestone3.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on GitHub and everywhere else. Images are only accepted from dev or prod, not localhost. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Orders will be able to be recorded </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Orders table with valid data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/236325852-6f444321-edaa-4757-bc8a-33a7ecbffae0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Missing first_name/last_name I forgot to include these with the initial db creation<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of OrderItems table with validate data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/236326243-6d6d626d-1c39-4554-82f7-87ce8f0efa3e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>IS601_OrderItems table<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the purchase form UI from Heroku</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/236328740-cd282073-7b00-4081-b520-d6404ec32484.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Checkout form<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot showing the items pending purchase from Heroku</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/236471608-fb76e6d2-76fd-4029-9f7b-996b62a9f88f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Pending purchase area is at the top of the checkout page, features a<br>back button to the cart. Does not display % change, I tried to<br>do cost in cart- product cost but could not get this to work.<br>Right now it just makes the user go back and update cart if<br>the price has changed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a screenshot showing the Order Process validations from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/236326981-bfb54942-f4e0-445c-9664-370e23f7505d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Verufy stick/price<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/236327135-1b42d9a3-747d-41e8-bb34-32bfdb4cbe18.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Verify paid amount vs cart amount<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/236472434-49327fd9-b113-4410-8bc6-cdcd1e6c4b34.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Verify address pieces (seems like this does not work perfectly but was attempted),<br>verifies payment method(have to choose one of the options given)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a screenshot showing the Order Process validations from the UI (Heroku)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/236328219-65b0e485-a847-43c2-996e-9f4d4e3bf39c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show invalid &quot;Money Received&quot; message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/236328533-3f8162ee-ae81-443f-ac92-566d261f8f52.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show unavailable stock message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/236329191-8603f3fd-d73d-40a6-9166-60dc73e6163d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show Price difference message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Briefly describe the code flow/process of the purchase process</td></tr>
<tr><td> <em>Response:</em> <div><ol><li>The user navigates to the checkout page, where the front end sends a<br>GET request to the '/shop/checkout' route. The backend checks if the user is<br>logged in using the @login_required decorator.<br></li><li>The backend calculates the total amount for all<br>the items in the user's cart by calling the get_cart_items function, which retrieves<br>cart items from the database and calculates their total cost.<br></li><li>The user fills out<br>the CheckoutForm and submits it. The front end sends a POST request to<br>the '/shop/checkout' route with the form data.<br></li><li>The backend validates the submitted form data.<br>If the form data is valid, it proceeds to process the order by<br>calling the process_order function. (This function handles tasks such as creating an order<br>record in the database, updating product stocks, and processing payments.)<br></li><li>If the order is<br>processed successfully, the backend sends a success message to the front end, redirecting<br>the user to the order confirmation page. If there's a problem with the<br>payment, the backend sends an error message to the front end, and the<br>user is asked to try again.<br></li></ol></div><br></td></tr>
<tr><td> <em>Sub-Task 8: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/GraceBurke-88/IS601-004/pull/71/commits/ede091edb231f2f6a95dd578710bf4cfce161e89">https://github.com/GraceBurke-88/IS601-004/pull/71/commits/ede091edb231f2f6a95dd578710bf4cfce161e89</a> </td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/GraceBurke-88/IS601-004/pull/71/commits/f2b1e4a3607138d228a04351db2312e0c1e146e4">https://github.com/GraceBurke-88/IS601-004/pull/71/commits/f2b1e4a3607138d228a04351db2312e0c1e146e4</a> </td></tr>
<tr><td> <em>Sub-Task 9: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td>Not provided</td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Order Confirmation Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot showing the order details from the purchase form and the related items that were purchased with a thank you message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/236474139-ad14c2a6-b5a4-4de9-ac87-7abe8656484f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows the order details, includes individual and total cost, shows total paid<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how this information is retrieved and displayed from a code logic perspective</td></tr>
<tr><td> <em>Response:</em> <div><ol><li>The front end sends a GET request to the '/shop/order_details/{order_id}' route, where the<br>'order_id' is the ID of the order that has just been processed.<br></li><li>The backend<br>checks if the user is logged in using the @login_required decorator.<br></li><li>The backend retrieves<br>the order details from the 'IS601_Orders' table in the database using the 'order_id'.<br>If the order doesn't exist or there's an issue with the query, an<br>error message is displayed.<br></li><li>Next, the backend retrieves the related order items from the<br>'IS601_OrderItems' table and joins them with the 'IS601_Products' table to include product names.<br>If there's an issue with this query, an error message is displayed.<br></li><li>The backend<br>calculates the total value of the order by summing the unit price multiplied<br>by the quantity of each order item.<br></li><li>The backend retrieves the payment method and<br>amount paid from the order details.<br></li><li>Finally, the backend renders the 'order_details.html' template and<br>sends the necessary information (order_id, order, order_items, total_value, payment_method, amount_paid) to the frontend.<br>The frontend displays the order details, order items, total value, payment method, and<br>amount paid on the order confirmation page.<br></li></ol></div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/GraceBurke-88/IS601-004/pull/71/commits/f2b1e4a3607138d228a04351db2312e0c1e146e4">https://github.com/GraceBurke-88/IS601-004/pull/71/commits/f2b1e4a3607138d228a04351db2312e0c1e146e4</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td>Not provided</td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> User will be able to see their Purchase History </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing purchase history for a user</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/236474881-00fb7226-03ac-4dad-a19c-a2fddad25328.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows order history for a user, can click on individual orders to see<br>history.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing full details of a purchase (Order Details Page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/236475007-cde20541-b046-4246-a05b-d16e9597beb6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows details of an order<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the logic for showing the purchase list and click/displaying the Order Details</td></tr>
<tr><td> <em>Response:</em> <div><ol><li>The code logic for showing the purchase list starts with a GET request<br>to the '/purchase_history' route.</li><li>&nbsp;The backend retrieves the user's order history from the database<br>and sends it to the front end, which displays the list.<br></li><li>When a user<br>clicks on order in the list, a GET request is sent to the<br>'/shop/order_details/{order_id}' route with the order ID.&nbsp;</li><li>The backend retrieves the order details and related<br>items from the database calculates the total value, and sends this information to<br>the frontend.&nbsp;</li><li>The front end then displays the order details page with the retrieved<br>information.<br></li></ol></div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/GraceBurke-88/IS601-004/pull/71/commits/2c80d470f056544e9f0801236931e370c6951c18">https://github.com/GraceBurke-88/IS601-004/pull/71/commits/2c80d470f056544e9f0801236931e370c6951c18</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td>Not provided</td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Store Owner Purchase History </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing purchase history from multiple users</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/236475706-d3a8c729-7b3a-4a73-b9d3-554c7780ed10.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows list of 10 most recent purchases. Shows the username, timestamp, etc., links<br>are clickable to see order details<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing full details of a purchase (Order Details Page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/236475773-91cbf0b1-97fb-43b8-afa0-20dbd024285c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Purchase by user1- shows order ID 92 in the URL<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the logic for showing the purchase list and click/displaying the Order Details (mostly how it differs from the user's purchase history feature)</td></tr>
<tr><td> <em>Response:</em> <div><ol><li>The logic for showing the purchase list for the admin starts with a<br>GET request to the '/shop/admin/purchase_history' route.&nbsp;<br></li><li>The @admin_permission decorator checks if the user has<br>admin permissions before proceeding.&nbsp;<br></li><li>The backend retrieves the order history for all users from<br>the database, including user IDs and usernames, and sends it to the frontend,<br>which displays the list.<br></li><li>When an admin clicks on an order in the list,<br>a GET request is sent to the '/shop/order_details/{order_id}' route with the order ID,<br>just like in the user's purchase history feature.&nbsp;<br></li><li>The backend retrieves the order details<br>and related items from the database, calculates the total value, and sends this<br>information to the frontend.&nbsp;<br></li><li>The front end then displays the order details page with<br>the retrieved information.&nbsp;<br></li><li>The main difference lies in the scope of orders displayed, where<br>the admin's purchase history feature shows orders for all users instead of just<br>the individual user.<br></li></ol></div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/GraceBurke-88/IS601-004/pull/71/commits/f5f0a292da7e8530b655dee11e93fdf1650a10ab">https://github.com/GraceBurke-88/IS601-004/pull/71/commits/f5f0a292da7e8530b655dee11e93fdf1650a10ab</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td>Not provided</td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart page showing the button to place an order</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/236330176-6927a09c-dc24-44d8-8472-5ef5aab68825.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Order button on cart page *edit is visible because this is the admin<br>logged in<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>The order check and confirmation pages gave me some trouble because I did<br>not realize I had to use a join at first, so I was<br>unsure how to get information from multiple tables to pass to the template.<br>I also had an issue with some of my functions, like calculating the<br>cart total and not knowing how to make them available to multiple routes.<br>I know that I have some repetitive parts to my code so ideally,<br>I would go back and combine some of that if I had more<br>time.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-3-shop-project/grade/gnb5" target="_blank">Grading</a></td></tr></table>