/*
 * javascript for index.html
 */
function validate(){
	var month = parseInt(document.getElementById("month").value);
	var day = parseInt(document.getElementById("day").value);
	var s_time = parseInt(document.getElementById("s_time").value);
	
	switch (month){
		case 1:
		case 3:
		case 5:
		case 7:
		case 8:
		case 10:
		case 12:
			if(!(day>=1 && day<=31)){
				alert("일 입력이 잘못 되었습니다.");
				return false;
			}
			break;
		case 4:
		case 6:
		case 9:
		case 11:
			if(!(day>=1 && day<=30)){
				alert("일 입력이 잘못 되었습니다.");
				return false;
			}
			break;
		case 2:
			if(!(day>=1 && day<=28))
				alert("일 입력이 잘못 되었습니다.");
				return false;
			break;
		default:
			alert("월 입력이 잘못 되었습니다.");
			return false;
	}
	
	if(!(s_time>=18 && s_time<=23)){
		alert("시간 입력이 잘못되었습니다.");
		return false;
	}
	
	return true;
}
