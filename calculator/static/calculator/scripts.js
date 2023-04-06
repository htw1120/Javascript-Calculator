function calculate() {
   let operand1 = parseFloat(document.getElementById("1stNumber").value)
   let operand2 = parseFloat(document.getElementById("2ndNumber").value)
   let dropdown = document.getElementById("operators")
   let operator = dropdown.value
   let negative = false
   let result = 0
   let test = false

      appendingDiv = document.getElementById("temporary")
   if (!['+', '-', '*', '/', '%', '**'].includes(operator)){
   test = true
   }

   else if (Math.sign(operand1) == -1 && operator=="**"){
        negative = true
   }
   else{
   result = eval(operand1 + operator + operand2)
   }




// Code partially taken from https://www.geeksforgeeks.org/how-to-create-a-form-dynamically-with-the-javascript/
   var form = document.createElement("form")


// Set up form
   form.setAttribute("method", "post")
   form.setAttribute("action", "index.html")

// Append to existing div
   appendingDiv.appendChild(form)


// Set up first operand
    var firstOperand = document.createElement("input")
    firstOperand.setAttribute("type", "hidden")
    firstOperand.setAttribute("id", "firstNumber")
    firstOperand.setAttribute("name", "firstNumber")
    firstOperand.setAttribute("value", operand1)


// Set up second operand
    var secondOperand = document.createElement("input")
    secondOperand.setAttribute("type", "hidden")
    secondOperand.setAttribute("id", "secondNumber")
    secondOperand.setAttribute("name", "secondNumber")
    secondOperand.setAttribute("value", operand2)


// Set up operator
    var oper = document.createElement("input")
    oper.setAttribute("type", "hidden")
    oper.setAttribute("id", "operator")
    oper.setAttribute("name", "operator")
    oper.setAttribute("value", operator)


// Set up result
    var result1 = document.createElement("input")
    result1.setAttribute("type", "hidden")
    result1.setAttribute("id", "result")
    result1.setAttribute("name", "result")
    result1.setAttribute("value", result)


// Set up save button
    var save = document.createElement("input")
    save.setAttribute("type", "submit")
    save.setAttribute("name", "Save")
    save.setAttribute("value", "Save")

    save.textContent="Save"

//  Set up delete button
    var remove1 = document.createElement("input")
    remove1.setAttribute("name", "Delete")
    remove1.setAttribute("type", "button")
    remove1.setAttribute("value", "x")
    remove1.addEventListener('click', () => remove1.parentNode.remove())

// Set up output expression
    var expression = document.createElement("span")
    expression.setAttribute("class", "expression")

    if ((Number.isNaN(operand1)) || (Number.isNaN(operand2))){
        expression.textContent = "Error - missing one or both operands."
        save.setAttribute("disabled", "true")
    }
    else if (negative){
    expression.textContent = "Error - You can't use exponents on negatives"
    save.setAttribute("disabled", "true")
    }

    else if (test){
        expression.textContent = "Error - operator isn't in the list of operators"
         save.setAttribute("disabled", "true")
}
    else if (Number.isNaN(result) || !isFinite(result)){
        expression.textContent = operand1 + " "
        expression.textContent += operator + " "
        expression.textContent += operand2 + " is undefined"
    }
    else{
        expression.textContent = operand1 + " "
        expression.textContent += operator + " "
        expression.textContent += operand2 + " = " + result
    }


// Set up token
    var token = document.getElementById("token")


// Append all to the form
    form.appendChild(firstOperand)
    form.appendChild(secondOperand)
    form.appendChild(oper)
    form.appendChild(result1)
    form.appendChild(save)
    form.appendChild(expression)
    form.appendChild(remove1)
    form.appendChild(token.cloneNode(true))











}



