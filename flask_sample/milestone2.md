<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Shop Project</td></tr>
<tr><td> <em>Student: </em> Grace Burke (gnb5)</td></tr>
<tr><td> <em>Generated: </em> 4/23/2023 4:08:20 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-2-shop-project/grade/gnb5" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Users with admin or shop owner will be able to add products </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of admin create item page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/233855403-a8e8d162-98a7-453c-beca-1378a32c5632.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Form for admin to add products<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of populated Products table clearly showing the columns</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/233855459-447ef135-9f12-479e-a5f4-5258b25aed81.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>IS601_Products table showing &#39;ProductName&#39; example<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly describe the code flow for creating a Product</td></tr>
<tr><td> <em>Response:</em> <div><ol><li>The User submits the "Add Product" form in the UI.&nbsp;<br></li><li>The form data is<br>sent as a POST request to the /add route.<br></li><li>The add() function in the<br>route checks if the submitted form data is valid.<br></li><li>If the form data is<br>valid, the function proceeds to insert the new product into the database using<br>an SQL INSERT statement.<br></li><li>The INSERT statement includes the product's name, description, stock, category,<br>cost and the active status.<br></li><li>The DB.insertOne() function is called to execute the SQL<br>query, inserting the new product into the database (IS601_Products).<br></li><li>If the insertion is successful,<br>a success message is flashed to the user. If an error occurs, an<br>error message is flashed instead.<br></li><li>The user is redirected to the appropriate page based<br>on the success or failure of the operation.<br></li></ol></div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/GraceBurke-88/IS601-004/pull/66/commits/bf8d68aaff829d42d443557da9da6a39fd952578">https://github.com/GraceBurke-88/IS601-004/pull/66/commits/bf8d68aaff829d42d443557da9da6a39fd952578</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="//shop.py">shop.py</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Any user can see visible products on the Shop Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Shop page showing 10 items without filters/sorting applied</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/233857266-a8034ccc-15bf-40f8-a1fa-081583512459.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Unfiltered shop page displaying 10 items<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Shop page showing both filters and a different sorting applied (should be more than 1 sample product)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/233857392-27e257ee-d782-490c-8a22-d8292f493692.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search by name &#39;w&#39;, allows for partial match<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/233857410-792ff296-06e4-4614-9538-5d6aa2f74d3b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Filter by category &#39;beverage&#39;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/233857419-3d2da368-0981-41c1-afa1-4d095a986af7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sort high-low<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/233857468-d4ee053d-f3ea-4044-8865-04fa37596b22.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Filter by name and sort high-low<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the filter/sort logic from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/233857637-7ed04198-bc44-4181-a3e5-12b32054e424.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing sorting/filtering logic<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Briefly explain how the results are shown and how the filters are applied</td></tr>
<tr><td> <em>Response:</em> <div><ol><li>Retrieve query parameters for name, category, order, and limit from the request.<br></li><li>Construct the<br>query to select products with visibility set to 1 (visible).<br></li><li>Apply the "name" filter<br>if provided, using the LIKE operator for partial matches.<br></li><li>Apply the "category" filter if<br>provided.<br></li><li>Apply the "order" option if provided, sorting the products by cost in ascending<br>or descending order.<br></li><li>Limit the number of results based on the "limit" parameter, ensuring<br>it's between 1 and 100.<br></li><li>Execute the query, store the results in the 'rows'<br>variable, and handle exceptions.<br></li><li>Retrieve unique categories for display, handling exceptions.<br></li><li>Render the "shop.html" template<br>with the fetched products and categories.<br></li></ol></div><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/GraceBurke-88/IS601-004/pull/66/commits/32b4fe02b1bcddd161db1bca1d186aee9e9d8a92">https://github.com/GraceBurke-88/IS601-004/pull/66/commits/32b4fe02b1bcddd161db1bca1d186aee9e9d8a92</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="//shop.py">shop.py</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Show Admin/Shop Owner Product List (this is not the Shop page and should show visibility status) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the Admin List page/results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/233856146-deefaece-40b3-4edc-85df-770e0ab80697.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Product list shows visible/not visible items, admin/products route<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the results are shown</td></tr>
<tr><td> <em>Response:</em> <div><ol><li>The route is defined with the endpoint /admin/products and accepts GET and POST<br>methods.<br></li><li>The admin_permission.require decorator is used to ensure that only users with admin permissions<br>can access this route.<br></li><li>The products() function is defined to handle the request.<br></li><li>An empty<br>list called rows is initialized to store the fetched products.<br></li><li>The database query logic<br>is wrapped inside a try block to handle any exceptions.<br></li><li>The DB.selectAll() method is<br>called with a SQL query to fetch product data.&nbsp;</li><li>The query selects the id,<br>name, description, stock, cost, image, and visibility columns from the IS601_Products table and<br>limits the result to 10 rows.<br></li><li>If the query execution is successful and there<br>are rows returned, the rows variable is set to the fetched product data.<br></li><li>If<br>any exceptions occur during the query execution, an error message is printed, and<br>a flash message with the "danger" category is displayed to inform the user<br>of the problem.<br></li><li>The fetched product data in the rows variable is passed to<br>the "products.html" template to be rendered.<br></li></ol></div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/GraceBurke-88/IS601-004/pull/66/commits/bf8d68aaff829d42d443557da9da6a39fd952578#diff-6cd7eb0f770d60d0a570dfd799d975b97541ac0e517a5b34c0aa0d568d1d6e66">https://github.com/GraceBurke-88/IS601-004/pull/66/commits/bf8d68aaff829d42d443557da9da6a39fd952578#diff-6cd7eb0f770d60d0a570dfd799d975b97541ac0e517a5b34c0aa0d568d1d6e66</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="//shop.py">shop.py</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin/Shop Owner Edit button </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the edit button visible to the Admin on the Shop page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/233856696-7792fc17-02ec-4ad5-80c9-19b7262f2ecf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit button visible to the Admin on the Shop page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the edit button visible to the Admin on the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/233856727-dc64a471-b3c3-4d1b-a9b9-8a20710803d9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit button for Admin use on product 1 page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot showing the edit button visible to the Admin on the Admin Product List Page (The admin page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/233856783-d50ee35f-2df2-4922-a9eb-19dc19d43065.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit button visible to the Admin on the Admin Product List Page (The<br>admin page)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after screenshot of Editing a Product via the Admin Edit Product Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/233856825-164fd75a-254e-4184-b42f-fcf588d7bbb6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before editing &#39;Product ex 2&#39;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/233856872-3f0d6b31-ac78-452a-bf9c-5ae0d5d6464d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After editing, now called &#39;Product2&#39; and other data updated, flash message shows successful<br>update<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <div><ol><li>Define the /admin/product route with GET and POST methods.<br></li><li>Use admin_permission decorator to restrict<br>access.<br></li><li>Initialize ProductForm instance and obtain product ID.<br></li><li>Set the type variable based on the<br>presence of the product ID.<br></li><li>If the form is submitted and valid:<br></li><li>Update the product<br>if there's an ID, or create a new one if not.<br></li><li>Display success or<br>error messages based on query execution.<br></li><li>If there's a product ID, fetch the product<br>data and populate the form.<br></li><li>Render the "product.html" template with the form and the<br>type.<br></li></ol></div><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/GraceBurke-88/IS601-004/pull/66/commits/ec9041a2bf6bde2eaa7026e682ec71a072e68088">https://github.com/GraceBurke-88/IS601-004/pull/66/commits/ec9041a2bf6bde2eaa7026e682ec71a072e68088</a> </td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="//shop.py">shop.py</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Product Details Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the button (clickable item) that directs the user to the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/233857835-cb03d072-1994-45d9-a508-2c92db45ca6b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Name is clickable (becomes underlined on hover) (Shown w/ &#39;Kooky Kale Krunchers&#39;)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the result of the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/233858027-ffc64a3b-b53c-49d3-9bf4-a5ea9c6d8053.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Product page after clicking on name<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <ol><li>Define a new route for the product details page with the path "/product/int:product_id"<br>and method "GET".<br></li><li>When the route is accessed, the product_page function is called with<br>the product_id parameter.<br></li><li>Execute a query to retrieve the product information (id, name, description,<br>stock, cost, image) from the database using the product_id.<br></li><li>If the query is successful<br>and a product is found:</li><ol><li>Assign the product data to the 'product' variable.</li><li>Render the<br>"product_page.html" template with the 'product' data.</li></ol><li>If the product is not found, show an<br>error message using flash and redirect the user to the main shop list<br>page.<br></li><li>If an exception occurs during the process, log the error, display an error<br>message, and redirect the user to the main shop list page.<br></li></ol><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/GraceBurke-88/IS601-004/pull/66/commits/bf8d68aaff829d42d443557da9da6a39fd952578#diff-6cd7eb0f770d60d0a570dfd799d975b97541ac0e517a5b34c0aa0d568d1d6e66">https://github.com/GraceBurke-88/IS601-004/pull/66/commits/bf8d68aaff829d42d443557da9da6a39fd952578#diff-6cd7eb0f770d60d0a570dfd799d975b97541ac0e517a5b34c0aa0d568d1d6e66</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file (can be any specific item)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="//shop.py">shop.py</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add to Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the success message of adding to cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/233858532-d8e15d32-ea71-4327-92f6-9bc1a6676a1c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success message of adding to cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the error message of adding to cart (i.e., when not logged in)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/233860820-4b1aede7-1e29-4d8b-b99d-788c155da6ed.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> error message of adding to cart (i.e., when not logged in)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Cart table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/233858680-500b543d-95f7-4048-888a-c62f8c2e44e3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart table with data in it (bottom two rows relate to user 3)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Tell how your cart works (1 cart per user; multiple carts per user)</td></tr>
<tr><td> <em>Response:</em> <p>1 cart per user<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Explain the process of add to cart</td></tr>
<tr><td> <em>Response:</em> <ol><li>Retrieve the required information from the form: product_id, id, quantity, and the user_id<br>of the current user.<br></li><li>Check if id and user_id are present and if the<br>quantity is greater than 0.<br></li><li>Execute a query to retrieve the product's cost and<br>name from the IS601_Products table using the id.<br></li><li>If the product_id is present (i.e.,<br>updating from the cart):<br></li><ol><li>Update the existing cart item's quantity and cost in the<br>IS601_Cart table.</li><li>Show a success message to indicate the quantity has been updated.</li></ol><li>If the<br>product_id is not present (i.e., adding from the shop):<br></li><ol><li>Insert a new row into<br>the IS601_Cart table with the product's details, or update the existing row if<br>there's already an entry for the same product and user.</li><li>Show a success message<br>to indicate the product has been added to the cart.</li></ol><li>If the quantity is<br>not greater than 0, assume the item should be deleted from the cart.<br></li><ol><li>Delete<br>the cart item from the IS601_Cart table.</li><li>Show a success message to indicate the<br>product has been removed from the cart.</li></ol><li>In case of any exceptions during the<br>above steps, log the error and show an error message using flash.<br></li><li>Retrieve the<br>cart items for the current user by executing a query that joins the<br>IS601_Cart and IS601_Products tables.<br></li><li>Render the "cart.html" template with the cart items' information.</li></ol><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/GraceBurke-88/IS601-004/pull/66/commits/32b4fe02b1bcddd161db1bca1d186aee9e9d8a92#diff-6cd7eb0f770d60d0a570dfd799d975b97541ac0e517a5b34c0aa0d568d1d6e66">https://github.com/GraceBurke-88/IS601-004/pull/66/commits/32b4fe02b1bcddd161db1bca1d186aee9e9d8a92#diff-6cd7eb0f770d60d0a570dfd799d975b97541ac0e517a5b34c0aa0d568d1d6e66</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> User will be able to see their Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart View</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/233858732-1f488264-c327-4246-a882-866671a0c23a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart page: shows subtotal, carry total, link to product details, several products<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the cart is being shown from a code perspective along with the subtotal and total calculations</td></tr>
<tr><td> <em>Response:</em> <div><ol><li>Retrieve cart items: Execute a SELECT query joining IS601_Cart and IS601_Products tables, calculating<br>the subtotal for each item.<br></li><li>Store query results: Save the retrieved cart items in<br>the rows variable.<br></li><li>Display cart items: Pass the rows variable to the "cart.html" template,<br>and iterate through it to display product details and subtotals.<br></li><li>Calculate total cost: In<br>the template, loop through the rows variable, summing up the subtotals to get<br>the total cost.<br></li><li>Display total cost: Show the calculated total cost in the appropriate<br>section of the "cart.html" template.<br></li></ol></div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/GraceBurke-88/IS601-004/pull/66/commits/32b4fe02b1bcddd161db1bca1d186aee9e9d8a92#diff-6cd7eb0f770d60d0a570dfd799d975b97541ac0e517a5b34c0aa0d568d1d6e66">https://github.com/GraceBurke-88/IS601-004/pull/66/commits/32b4fe02b1bcddd161db1bca1d186aee9e9d8a92#diff-6cd7eb0f770d60d0a570dfd799d975b97541ac0e517a5b34c0aa0d568d1d6e66</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="//shop.py">shop.py</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> User can update cart quantity </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a before and after screenshot of Cart Quantity update</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/233858741-c3cac2c5-92da-44aa-b9b6-f5f9e963ef1e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before updating quantity<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/233858756-34e0a3b6-7985-447b-906a-596151eeedde.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After updating quantity<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a before and after screenshot of setting Cart Quantity to 0</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/233859336-2f61db3b-a891-4879-9fdb-3b9ed7da9f26.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> before  screenshot of setting Cart Quantity to 0<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/233859336-2f61db3b-a891-4879-9fdb-3b9ed7da9f26.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after screenshot of setting Cart Quantity to 0<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how a negative quantity is handled</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/233858812-e206394b-56b7-4218-89bb-fe88bf76bb68.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show how a negative quantity is handled<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/233858827-4e3c55c2-8e2d-467a-bb42-9f9e84a22a1d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Item is deleted <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain the update process including how a value of 0 and negatives are handled</td></tr>
<tr><td> <em>Response:</em> <div><ol><li>Check if the updated quantity is greater than 0:<br></li><ol><li>If the quantity is greater<br>than 0, update the cart item with the new quantity and cost.</li><li>If the<br>quantity is 0 or negative, assume the user wants to delete the item<br>from the cart.</li></ol><li>For updating the cart item:<br></li><ol><li>Execute an UPDATE query to set the<br>new quantity and cost in the IS601_Cart table.</li><li>Show a success message indicating the<br>updated quantity for the item.</li></ol><li>For deleting the item from the cart:<br></li><ol><li>Execute a DELETE<br>query to remove the item from the IS601_Cart table based on the product_id<br>and user_id.</li><li>Show a success message indicating the item has been removed from the<br>cart.</li></ol></ol></div><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/GraceBurke-88/IS601-004/pull/66/commits/32b4fe02b1bcddd161db1bca1d186aee9e9d8a92#diff-6cd7eb0f770d60d0a570dfd799d975b97541ac0e517a5b34c0aa0d568d1d6e66">https://github.com/GraceBurke-88/IS601-004/pull/66/commits/32b4fe02b1bcddd161db1bca1d186aee9e9d8a92#diff-6cd7eb0f770d60d0a570dfd799d975b97541ac0e517a5b34c0aa0d568d1d6e66</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Cart Item Removal </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a before and after screenshot of deleting a single item from the Cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/233858857-d434dd7f-606a-4ef6-9225-19b416cd1995.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart before removal<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/233858864-18540a77-785c-4b03-aac8-9c91bf2be344.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Deleted item &#39;Sea-Sational Smoothies&#39;<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after screenshot of clearing the cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/233858864-18540a77-785c-4b03-aac8-9c91bf2be344.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before clearing the cart<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/70772404/233858882-28f720de-25ed-48d0-a9cc-773bb281ca17.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After clearing cart (button in left bottom)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how each delete process works</td></tr>
<tr><td> <em>Response:</em> <ol><li>Deleting a single item from the cart:<br></li><ul><li>Identify the product_id and user_id associated with<br>the cart item.</li><li>Execute a DELETE query to remove the item from the IS601_Cart<br>table based on the product_id and user_id.</li><li>Show a success message indicating the item<br>has been removed from the cart.</li></ul><li>Clearing the entire cart:<br></li><ul><li>Identify the user_id associated with<br>the cart items.</li><li>Execute a DELETE query to remove all items from the IS601_Cart<br>table for the specified user_id.</li><li>Show a success message indicating that the entire cart<br>has been cleared.</li></ul></ol><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/GraceBurke-88/IS601-004/pull/66/commits/32b4fe02b1bcddd161db1bca1d186aee9e9d8a92#diff-6cd7eb0f770d60d0a570dfd799d975b97541ac0e517a5b34c0aa0d568d1d6e66">https://github.com/GraceBurke-88/IS601-004/pull/66/commits/32b4fe02b1bcddd161db1bca1d186aee9e9d8a92#diff-6cd7eb0f770d60d0a570dfd799d975b97541ac0e517a5b34c0aa0d568d1d6e66</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>I had some issues with my database because the initial table I created<br>for IS601_Products was missing some columns. To fix this I tried adding an<br>sql file to modify the table. However, this did not work so I<br>had to manually fix the two columns and their types. Not ideal, but<br>got the database working correctly. I also had an issue with some of<br>the bootstrap formatting-- which I am still messing around. The bootstrap documentation on<br>the site is pretty helpful so I used that to make the layout<br>and UI better.&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td>Not provided</td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-2-shop-project/grade/gnb5" target="_blank">Grading</a></td></tr></table>