function calcular(operacao) {
    const campo1 = document.getElementById("num1");
    const campo2 = document.getElementById("num2");
    const resultado = document.getElementById("resul");

    const valor1Texto = campo1.value.trim();
    const valor2Texto = campo2.value.trim();

    if (valor1Texto === "" || isNaN(valor1Texto)) {
        alert("Digite um número válido no campo Número 1.");
        campo1.value = "";
        campo1.focus();
        return;
    }

    if (valor2Texto === "" || isNaN(valor2Texto)) {
        alert("Digite um número válido no campo Número 2.");
        campo2.value = "";
        campo2.focus();
        return;
    }

    const valor1 = parseFloat(valor1Texto);
    const valor2 = parseFloat(valor2Texto);

    let resultadoFinal;

    switch (operacao) {
        case "+":
            resultadoFinal = valor1 + valor2;
            break;

        case "-":
            resultadoFinal = valor1 - valor2;
            break;

        case "x":
            resultadoFinal = valor1 * valor2;
            break;

        case ":":
            if (valor2 === 0) {
                alert("Não é possível dividir por zero.");
                campo2.value = "";
                campo2.focus();
                return;
            }

            resultadoFinal = valor1 / valor2;
            break;

        default:
            return;
    }

    resultado.value = resultadoFinal.toFixed(2);
}


function limpar() {
    document.getElementById("num1").focus();
}


const botoesOperacao = document.querySelectorAll("[data-operacao]");

botoesOperacao.forEach(function (botao) {
    botao.addEventListener("click", function () {
        const operacao = botao.dataset.operacao;

        calcular(operacao);
    });
});


const calculadora = document.getElementById("calculator");

calculadora.addEventListener("reset", function () {
    setTimeout(function () {
        limpar();
    }, 0);
});

let player;

const videoId = "qaWvI8lstgg";

function onYouTubeIframeAPIReady() {
    player = new YT.Player("youtube-player", {
        videoId: videoId,

        playerVars: {
            autoplay: 0,
            controls: 0,
            loop: 1,
            playlist: videoId,
            rel: 0,
            modestbranding: 1
        },

        events: {
            onReady: function () {
                player.setVolume(70);
            }
        }
    });
}


const music = document.getElementById("music");

music.addEventListener("click", function () {
    if (!player) {
        return;
    }

    const estadoAtual = player.getPlayerState();

    if (estadoAtual === YT.PlayerState.PLAYING) {
        player.pauseVideo();
        music.textContent = "♫ PLAY";
    } else {
        player.playVideo();
        music.textContent = "♫ PAUSE";
    }
});
