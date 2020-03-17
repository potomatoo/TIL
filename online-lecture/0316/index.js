const form = document.querySelector('form');
const users = ['admin', 'ssafy', 'test'];

form.addEventListener('submit', function(event) {
  // 각 변수에 담기 위한 코드 입니다. 수정을 금합니다.
  event.preventDefault();
  const formData = new FormData(event.currentTarget);
  const userName = formData.get('username');
  const password = formData.get('password');
  const passwordConfirmation = formData.get('password_confirmation');
  // 개발자 도구를 통해 해당 값들을 모두 확인하세요.
  console.log(userName, password, passwordConfirmation);
  // 위의 값들을 활용하여, 회원가입 로직을 작성하시오.
  var flag = 1;
  for(var i = 0; i < users.length; i++){
    if(users[i] == userName){
      flag = 0
      alert("아이디가 중복되었습니다.");
    } 
  }

  if(password != passwordConfirmation){
    flag = 0
    alert("비밀번호가 일치하지 않습니다.");
  }
  
  if(flag == 1){
    alert(userName + "님, 회원가입을 축하드립니다.");
  }
})
