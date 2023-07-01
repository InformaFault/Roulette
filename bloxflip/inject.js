(function () {
    document.onkeyup = function () {
        var a = a || window.event; // for IE to cover IEs window event-object
        if (a.altKey && a.which == 65) {
            var div = document.createElement('div');
            div.id = "panel";

            if (document.body.contains(document.getElementById('panel'))) {

                document.getElementById('panel').remove()

            } else {

                document.body.appendChild(div);


                const head = document.head || document.getElementsByTagName('head')[0];
                var panel = document.getElementById("panel");


                // move the panel
                var isDragging = false;
                var offsetX = 0;
                var offsetY = 0;


                panel.addEventListener("mousedown", function (e) {
                    isDragging = true;
                    offsetX = e.offsetX;
                    offsetY = e.offsetY;
                });


                document.addEventListener("mousemove", function (e) {
                    if (isDragging) {
                        panel.style.left = (e.clientX - offsetX) + "px";
                        panel.style.top = (e.clientY - offsetY) + "px";
                    }
                });


                document.addEventListener("mouseup", function (e) {
                    isDragging = false;
                });


                // PANEL LOGIN

                var title = document.createElement("h1");
                title.innerHTML = 'Injection Login';
                title.id = "Title";


                var passCode = document.createElement("input");
                passCode.id = "passCodeInput"
                passCode.type = 'password'


                var submitPassCode = document.createElement("button")
                submitPassCode.id = "submitPassCode"
                submitPassCode.innerHTML = 'Submit';
                

                document.getElementById("panel").append(title);             // title
                document.getElementById("panel").append(passCode);          // passCode
                document.getElementById("panel").append(submitPassCode);    // submitPassCode

                submitPassCode.addEventListener("click", function () {
                    var code = passCode.value;
                    console.log(code);
                });

                document.getElementById("Title").remove();
                document.getElementById("passCodeInput").remove();
                document.getElementById("submitPassCode").remove();

                /*                  
                                /!\ SECRET /!\ 
                */

                // charge element
                var title = document.createElement("h1");
                title.innerHTML = '__Bloxflip__';
                title.id = "Title";

                document.getElementById("panel").append(title);


                var autoFarmSlideLabel = document.createElement("label");
                var autoFarmSlideInput = document.createElement("input");
                var autoFarmSlideSpan = document.createElement("span");
                autoFarmSlideLabel.className = "switch";
                autoFarmSlideInput.type = "checkbox";
                autoFarmSlideInput.id = "toggle-01";
                autoFarmSlideSpan.className = "slider round";

                autoFarmSlideLabel.appendChild(autoFarmSlideInput);
                autoFarmSlideLabel.appendChild(autoFarmSlideSpan);

                panel.appendChild(autoFarmSlideLabel);

                autoFarmSlideText = document.createElement("p")
                autoFarmSlideText.id = "textSlide"

                


                const links = document.querySelectorAll('a.sidebar_sidebarGamesLink__9ctbj');

                links.forEach(link => {
                    if (link.getAttribute('href').includes('/roulette')) {
                        link.click();
                    }
                });

                const inputElement = document.querySelector('.input_input__uGeT_');
                inputElement.value = '30';
                const event = new Event('input', { bubbles: true });
                const timeout = 100;

                [...Array(inputElement.value.length)].forEach((_, index) => {

                    setTimeout(() => {
                    const key = inputElement.value[index];
                    const eventArgs = {

                    bubbles: true,
                    keyCode: key.charCodeAt(),
                    which: key.charCodeAt()

                    };
                    inputElement.dispatchEvent(new KeyboardEvent('keydown', eventArgs));
                    inputElement.dispatchEvent(new KeyboardEvent('keypress', eventArgs));
                    inputElement.dispatchEvent(new KeyboardEvent('input', eventArgs));
                    inputElement.dispatchEvent(new KeyboardEvent('keyup', eventArgs));
                    }, timeout * index);

                });

                inputElement.value = '1';

                
                

                
                (function() {
                    var checkExist = setInterval(function() {
                      var gameStatus = document.querySelector('.roulette_rouletteGameStatus__kOoVo');
                      if (gameStatus && gameStatus.textContent === 'Rolling in 15s') {
                        clearInterval(checkExist);

                        setTimeout(() => {
                            document.querySelector('button.button_button__eJwei.button_primary__mdLFG.gameBetSubmit').click();
                        }, 500); // 2 secondes d'attente avant de cliquer sur le bouton
                      }
                    }, 100); // Vérifiez toutes les 100 ms si la div avec la classe roulette_rouletteGameStatus__kOoVo contient le texte "Rolling in 15s"
                  })();
                  



            }

            return false;
        }

    }

})();
