 // get the headong element
 const headingEl = document.querySelector("#headingTotal");

 //get the desc to refrence element
 const inputDescEl= document.querySelector("#inputDescription");

 // get the amount element
 const inputElement = document.querySelector("#inputAmount");

 //get expenseTable div
 const expenseTableEl = document.querySelector("#expenseTable")

 // init value of expense at 0
 let totalExpense=0;

 // set the heading element to total expense
 headingEl.textContent = `Total : ${totalExpense}`;

 // allexpenses at one place
 let allexpenses = [];

 // on ButtonClick add input to total Expense
 function addExpenseTotal() {
     
     // create a object
     const expenseItem ={};

     // read the input desc
     const textDesc = inputDescEl.value;

     // convert it to number
     const textAmount = inputElement.value;
     const expense = parseInt(textAmount);

     //put it in object
     expenseItem.desc  = textDesc;
     expenseItem.amount = expense;
     expenseItem.moment = new Date;

     //put the object in the array
     allexpenses.push(expenseItem);

     // console.clear();
     // console.table(allexpenses);
     // add to total expense
     totalExpense  += expense;
     const sometext = `Total : ${totalExpense}`; //templating
     // set heading element to total expense
     headingEl.textContent = sometext;   
     
     // show table here
     // const data1 = allexpenses[0];
     // const data2 = allexpenses[1];
     
     // const data1Text = `${data1.amount} :: ${data2.desc}`;
     // const data2Text = `${data2.amount} :: ${data2.desc}`;
     
     // // templating 
     // const tableText = `
     // <div>${data1Text}</div>
     // <div>${data2Text}</div>
     // `

     renderList(allexpenses);

 }
  
 // get the button element
 const element = document.querySelector("#btnAddExpense ") // dom here then selecter we have # id or . class              

 // Listen to click 
 element.addEventListener("click" , addExpenseTotal, false); // callback function

 // Controller functions
 function getDateString(moment){
     return moment.toLocaleDateString('en-US' ,{ 
         year: 'numeric',
         month: 'long',
         day: 'numeric'
     })
 }
 
 function deleteItem(dateValue , amount) {
     console.log("hihih");
     const filterArr = allexpenses
                         .filter(expense => expense.moment.valueOf() !== dateValue );
     
     allexpenses = filterArr;
     renderList(filterArr);
     totalExpense -= amount;
     headingEl.textContent = `Total : ${totalExpense}`;
     
 }

 function renderList(arrOfList){
     const allexpensesHTML = arrOfList.map(expense => createList(expense)).join("");
     expenseTableEl.innerHTML = allexpensesHTML;
 }

 // View Layer
 function createList({desc , amount , moment}){
     return `
         <li class="list-group-item d-flex justify-content-between">
             <div class="d-flex flex-column">
                 ${desc}
                 <small class="text-muted">${getDateString(moment)}</small>
             </div>
             <div>
                 <span class="px-5">
                     ${amount} 
                 </span>
                 <button 
                     onclick="deleteItem(${moment.valueOf()} , ${amount})"
                     type="button" 
                     class="btn btn-outline-danger btn-sm">
                     <i class="fas fa-trash-alt"></i>
                 </button>
             </div>
         </li>
     `;
 }
