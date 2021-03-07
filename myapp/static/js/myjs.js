	function checkfname()
		{
			let f=document.signup.fname.value;
			let reg=/^[A-Za-z]+$/;
			if(f=="")
			{
				document.getElementById("fname").innerHTML="Please Enter First Name";
				document.getElementById("btn").disabled="true";
			}
			else if(!reg.test(f))
			{
				document.getElementById("fname").innerHTML="Plese Enter Only Alphabets";
				document.getElementById("btn").disabled="true";
			}
			else
			{
				document.getElementById("fname").innerHTML="";
				document.getElementById("btn").disabled="";
			}
	
		}
		function checklname()
		{
			let l=document.signup.lname.value;
			let reg=/^[A-Za-z]+$/;
			if(l=="")
			{
				document.getElementById("lname").innerHTML="Plese Enter Last Name";
				document.getElementById("btn").disabled="true";
			}
			else if(!reg.test(l))
			{
				document.getElementById("lname").innerHTML="Plese Enter Only Alphabets";
				document.getElementById("btn").disabled="true";
			}
			else
			{
				document.getElementById("lname").innerHTML="";
				document.getElementById("btn").disabled="";
			}

		}
		function checkemail()
		{
			let e=document.signup.email.value;
			let reg=/^[A-Za-z0-9-_.]+@[A-za-z]+\.[A-za-z]{2,4}$/;
			if(e=="")
			{
				document.getElementById("email").innerHTML="Plese Enter Email";
				document.getElementById("btn").disabled="true";
			}
			else if(!reg.test(e))
			{
				document.getElementById("email").innerHTML="Plese Enter valid email";
				document.getElementById("btn").disabled="true";
			}
			else
			{
				document.getElementById("email").innerHTML="";
				document.getElementById("btn").disabled="";
			}

		}
		function checkmobile()
		{
			let m=document.signup.mobile.value;
			let reg=/^\d{10}$/;
			if(m=="")
			{
				document.getElementById("mobile").innerHTML="Plese Enter Moblie";
				document.getElementById("btn").disabled="true";
			}
			else if(!reg.test(m))
			{
				document.getElementById("mobile").innerHTML="Plese Enter 10 Digit";
				document.getElementById("btn").disabled="true";
			}
			else
			{
				document.getElementById("mobile").innerHTML="";
				document.getElementById("btn").disabled="";
			}

		}
		function checkpass()
		{

			let p=document.signup.password.value;
			let reg=/^[A-Za-z0-9_@$#%^&+=!]{8,15}$/;
			//let regp=/^(?=.*[a-z])(?=.*[A-z])(?=.*\d))(?=.*[_@$#%^&+=*!])[A-Za-z\d@$!#%*&?]{8,20}$/;
			if(p=="")
			{
				document.getElementById("password").innerHTML="Plese Enter Password";
				document.getElementById("btn").disabled="true";
			}
			else if(!reg.test(p))
			{
				document.getElementById("password").innerHTML="Plese Enter valid Password";
				document.getElementById("btn").disabled="true";
			}
			else
			{
				document.getElementById("password").innerHTML="";
				document.getElementById("btn").disabled="";
			}

		}