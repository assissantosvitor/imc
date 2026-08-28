import webbrowser
import os
import tempfile

def criar_arquivos():
    temp_dir = tempfile.gettempdir()
    
    # ==================== PÁGINA DO EASTER EGG ====================
    easter_html = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Easter Egg - Piettro Gostosão</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
            font-family: 'Segoe UI', system-ui, sans-serif;
            overflow: hidden;
            color: white;
        }
        
        .container {
            text-align: center;
            z-index: 10;
            animation: fadeIn 1.2s ease;
        }
        
        h1 {
            font-size: 3.2rem;
            background: linear-gradient(90deg, #ff6b6b, #feca57, #48dbfb, #ff9ff3);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 20px;
            animation: glow 2s ease-in-out infinite alternate;
        }
        
        .subtitle {
            font-size: 1.5rem;
            color: #f8f9fa;
            margin-bottom: 25px;
            opacity: 0.9;
        }
        
        .badge {
            display: inline-block;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 12px 28px;
            border-radius: 50px;
            font-size: 1.15rem;
            animation: pulse 2s infinite;
        }
        
        .emoji {
            font-size: 4.5rem;
            margin-bottom: 15px;
            animation: bounce 1.5s infinite;
        }
        
        .particles {
            position: absolute;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            overflow: hidden;
            z-index: 1;
        }
        
        .particle {
            position: absolute;
            border-radius: 50%;
            animation: fall linear infinite;
            opacity: 0.7;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        @keyframes glow {
            from { filter: brightness(1); }
            to { filter: brightness(1.25); }
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.06); }
        }
        
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-18px); }
        }
        
        @keyframes fall {
            to { transform: translateY(100vh) rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="particles" id="particles"></div>
    
    <div class="container">
        <div class="emoji">🥚✨</div>
        <h1>Você encontrou o Easter Egg!</h1>
        <p class="subtitle">Do lendário <strong>Piettro Gostosão</strong></p>
        <div class="badge">🔥 Piettro Gostosão 🔥</div>
        <p style="opacity: 0.55; font-size: 0.95rem; margin-top: 40px;">
            Calculadora de IMC • Edição Secreta
        </p>
    </div>

    <script>
        const container = document.getElementById('particles');
        const colors = ['#ff6b6b', '#feca57', '#48dbfb', '#ff9ff3', '#1dd1a1', '#f368e0'];
        
        for (let i = 0; i < 55; i++) {
            const p = document.createElement('div');
            p.classList.add('particle');
            p.style.left = Math.random() * 100 + 'vw';
            p.style.background = colors[Math.floor(Math.random() * colors.length)];
            p.style.animationDuration = (Math.random() * 3 + 2) + 's';
            p.style.animationDelay = Math.random() * 5 + 's';
            const size = Math.random() * 7 + 4;
            p.style.width = p.style.height = size + 'px';
            container.appendChild(p);
        }
    </script>
</body>
</html>
"""

    # ==================== CALCULADORA DE IMC ====================
    calc_html = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora de IMC</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: linear-gradient(145deg, #0f172a, #1e293b);
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
            padding: 20px;
            color: #e2e8f0;
        }
        
        .card {
            background: rgba(30, 41, 59, 0.85);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(148, 163, 184, 0.15);
            border-radius: 24px;
            padding: 40px 36px;
            width: 100%;
            max-width: 420px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            animation: slideUp 0.6s ease;
        }
        
        @keyframes slideUp {
            from { opacity: 0; transform: translateY(25px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        h1 {
            text-align: center;
            font-size: 1.85rem;
            font-weight: 700;
            margin-bottom: 8px;
            background: linear-gradient(90deg, #38bdf8, #818cf8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .subtitle {
            text-align: center;
            color: #94a3b8;
            font-size: 0.95rem;
            margin-bottom: 32px;
        }
        
        .form-group {
            margin-bottom: 22px;
        }
        
        label {
            display: block;
            font-size: 0.9rem;
            color: #94a3b8;
            margin-bottom: 8px;
            font-weight: 500;
        }
        
        input {
            width: 100%;
            padding: 14px 16px;
            background: #0f172a;
            border: 1px solid #334155;
            border-radius: 12px;
            color: #f1f5f9;
            font-size: 1.05rem;
            transition: all 0.25s ease;
            outline: none;
        }
        
        input:focus {
            border-color: #38bdf8;
            box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.2);
        }
        
        input::placeholder {
            color: #475569;
        }
        
        button {
            width: 100%;
            padding: 15px;
            background: linear-gradient(135deg, #3b82f6, #6366f1);
            border: none;
            border-radius: 12px;
            color: white;
            font-size: 1.05rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.25s ease;
            margin-top: 8px;
        }
        
        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px -5px rgba(99, 102, 241, 0.4);
        }
        
        button:active {
            transform: translateY(0);
        }
        
        .resultado {
            margin-top: 28px;
            padding: 22px;
            background: #0f172a;
            border-radius: 16px;
            text-align: center;
            display: none;
            animation: fadeIn 0.4s ease;
        }
        
        .resultado.show {
            display: block;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: scale(0.96); }
            to { opacity: 1; transform: scale(1); }
        }
        
        .imc-valor {
            font-size: 2.8rem;
            font-weight: 700;
            color: #38bdf8;
            margin-bottom: 6px;
        }
        
        .classificacao {
            font-size: 1.15rem;
            font-weight: 500;
            margin-top: 4px;
        }
        
        .easter-btn {
            margin-top: 24px;
            background: transparent;
            border: 1px dashed #475569;
            color: #64748b;
            font-size: 0.85rem;
            padding: 10px;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.25s ease;
        }
        
        .easter-btn:hover {
            border-color: #f472b6;
            color: #f472b6;
            background: rgba(244, 114, 182, 0.08);
            transform: none;
            box-shadow: none;
        }
        
        .footer {
            text-align: center;
            margin-top: 20px;
            font-size: 0.8rem;
            color: #475569;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>Calculadora de IMC</h1>
        <p class="subtitle">Descubra seu Índice de Massa Corporal</p>
        
        <div class="form-group">
            <label for="peso">Peso (kg)</label>
            <input type="number" id="peso" placeholder="Ex: 70.5" step="0.1" min="1">
        </div>
        
        <div class="form-group">
            <label for="altura">Altura (metros)</label>
            <input type="number" id="altura" placeholder="Ex: 1.75" step="0.01" min="0.5" max="2.5">
        </div>
        
        <button onclick="calcular()">Calcular IMC</button>
        
        <div class="resultado" id="resultado">
            <div class="imc-valor" id="imcValor">—</div>
            <div class="classificacao" id="classificacao">—</div>
        </div>
        
        <button class="easter-btn" onclick="abrirEasterEgg()">🥚 Easter Egg</button>
        
        <p class="footer">Feito com ❤️</p>
    </div>

    <script>
        function calcular() {
            const peso = parseFloat(document.getElementById('peso').value.replace(',', '.'));
            const altura = parseFloat(document.getElementById('altura').value.replace(',', '.'));
            const resultadoDiv = document.getElementById('resultado');
            const imcValor = document.getElementById('imcValor');
            const classificacaoEl = document.getElementById('classificacao');
            
            if (!peso || !altura || peso <= 0 || altura <= 0) {
                alert('Por favor, preencha peso e altura com valores válidos.');
                return;
            }
            
            const imc = peso / (altura * altura);
            const imcArredondado = imc.toFixed(2);
            
            let texto, cor;
            
            if (imc < 18.5) {
                texto = '🔵 Abaixo do peso';
                cor = '#38bdf8';
            } else if (imc < 25) {
                texto = '🟢 Peso normal';
                cor = '#4ade80';
            } else if (imc < 30) {
                texto = '🟡 Sobrepeso';
                cor = '#facc15';
            } else if (imc < 35) {
                texto = '🟠 Obesidade grau 1';
                cor = '#fb923c';
            } else if (imc < 40) {
                texto = '🔴 Obesidade grau 2';
                cor = '#f87171';
            } else {
                texto = '⚫ Obesidade grau 3 (mórbida)';
                cor = '#a3a3a3';
            }
            
            imcValor.textContent = imcArredondado;
            imcValor.style.color = cor;
            classificacaoEl.textContent = texto;
            resultadoDiv.classList.add('show');
        }
        
        document.querySelectorAll('input').forEach(input => {
            input.addEventListener('keypress', function(e) {
                if (e.key === 'Enter') calcular();
            });
        });
        
        function abrirEasterEgg() {
            window.open('easter_egg_piettro.html', '_blank');
        }
    </script>
</body>
</html>
"""

    caminho_calc = os.path.join(temp_dir, "calculadora_imc.html")
    caminho_easter = os.path.join(temp_dir, "easter_egg_piettro.html")
    
    with open(caminho_calc, "w", encoding="utf-8") as f:
        f.write(calc_html)
    
    with open(caminho_easter, "w", encoding="utf-8") as f:
        f.write(easter_html)
    
    return caminho_calc


if __name__ == "__main__":
    print("Abrindo a Calculadora de IMC no navegador...")
    caminho = criar_arquivos()
    webbrowser.open_new_tab(f"file://{caminho}")
    print("Calculadora aberta com sucesso!")
    print("Clique no botão 🥚 Easter Egg para abrir o segredo em outra guia.")