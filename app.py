from flask import Flask, render_template_string, request, jsonify
import webbrowser
import threading

app = Flask(__name__)

# ==================== FRONTEND - CALCULADORA ====================
CALC_HTML = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora de IMC</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
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
            background: rgba(30, 41, 59, 0.9);
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
            margin-bottom: 28px;
        }
        
        .form-group {
            margin-bottom: 20px;
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
        
        .btn-calcular {
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
            margin-top: 6px;
        }
        
        .btn-calcular:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px -5px rgba(99, 102, 241, 0.4);
        }
        
        .btn-calcular:active {
            transform: translateY(0);
        }
        
        .btn-calcular:disabled {
            opacity: 0.6;
            cursor: not-allowed;
            transform: none;
        }
        
        .resultado {
            margin-top: 26px;
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
            margin-bottom: 6px;
        }
        
        .classificacao {
            font-size: 1.15rem;
            font-weight: 500;
        }
        
        .erro {
            color: #f87171;
            font-size: 0.9rem;
            margin-top: 12px;
            text-align: center;
            display: none;
        }
        
        .easter-btn {
            margin-top: 22px;
            width: 100%;
            background: transparent;
            border: 1px dashed #475569;
            color: #64748b;
            font-size: 0.85rem;
            padding: 11px;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.25s ease;
        }
        
        .easter-btn:hover {
            border-color: #f472b6;
            color: #f472b6;
            background: rgba(244, 114, 182, 0.08);
        }
        
        .footer {
            text-align: center;
            margin-top: 18px;
            font-size: 0.8rem;
            color: #475569;
        }
        
        .backend-badge {
            text-align: center;
            font-size: 0.75rem;
            color: #64748b;
            margin-top: 14px;
            padding: 6px 12px;
            background: rgba(56, 189, 248, 0.08);
            border-radius: 20px;
            display: inline-block;
            width: 100%;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>Calculadora de IMC</h1>
        <p class="subtitle">Frontend + Backend em Python</p>
        
        <div class="form-group">
            <label for="peso">Peso (kg)</label>
            <input type="number" id="peso" placeholder="Ex: 70.5" step="0.1" min="1">
        </div>
        
        <div class="form-group">
            <label for="altura">Altura (metros)</label>
            <input type="number" id="altura" placeholder="Ex: 1.75" step="0.01" min="0.5" max="2.5">
        </div>
        
        <button class="btn-calcular" id="btnCalcular" onclick="calcular()">Calcular IMC</button>
        
        <div class="erro" id="erro"></div>
        
        <div class="resultado" id="resultado">
            <div class="imc-valor" id="imcValor">—</div>
            <div class="classificacao" id="classificacao">—</div>
        </div>
        
        <button class="easter-btn" onclick="abrirEasterEgg()">🥚 Easter Egg</button>
        
        <div class="backend-badge">⚡ Cálculo feito no Backend (Python/Flask)</div>
        <p class="footer">Feito com ❤️</p>
    </div>

    <script>
        async function calcular() {
            const peso = document.getElementById('peso').value.replace(',', '.');
            const altura = document.getElementById('altura').value.replace(',', '.');
            const btn = document.getElementById('btnCalcular');
            const erroEl = document.getElementById('erro');
            const resultadoDiv = document.getElementById('resultado');
            
            erroEl.style.display = 'none';
            resultadoDiv.classList.remove('show');
            
            if (!peso || !altura) {
                erroEl.textContent = 'Preencha peso e altura.';
                erroEl.style.display = 'block';
                return;
            }
            
            btn.disabled = true;
            btn.textContent = 'Calculando...';
            
            try {
                const response = await fetch('/api/calcular', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        peso: parseFloat(peso),
                        altura: parseFloat(altura)
                    })
                });
                
                const data = await response.json();
                
                if (!response.ok) {
                    throw new Error(data.erro || 'Erro no servidor');
                }
                
                document.getElementById('imcValor').textContent = data.imc;
                document.getElementById('imcValor').style.color = data.cor;
                document.getElementById('classificacao').textContent = data.classificacao;
                resultadoDiv.classList.add('show');
                
            } catch (err) {
                erroEl.textContent = err.message;
                erroEl.style.display = 'block';
            } finally {
                btn.disabled = false;
                btn.textContent = 'Calcular IMC';
            }
        }
        
        document.querySelectorAll('input').forEach(input => {
            input.addEventListener('keypress', function(e) {
                if (e.key === 'Enter') calcular();
            });
        });
        
        function abrirEasterEgg() {
            window.open('/easter', '_blank');
        }
    </script>
</body>
</html>
"""

# ==================== FRONTEND - EASTER EGG ====================
EASTER_HTML = """
<!DOCTYPE html>
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
            Calculadora de IMC • Frontend + Backend
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

# ==================== BACKEND (Python / Flask) ====================

@app.route("/")
def index():
    return render_template_string(CALC_HTML)


@app.route("/easter")
def easter():
    return render_template_string(EASTER_HTML)


@app.route("/api/calcular", methods=["POST"])
def calcular_imc():
    dados = request.get_json()
    
    if not dados:
        return jsonify({"erro": "Dados não enviados"}), 400
    
    try:
        peso = float(dados.get("peso", 0))
        altura = float(dados.get("altura", 0))
    except (TypeError, ValueError):
        return jsonify({"erro": "Valores inválidos"}), 400
    
    if peso <= 0 or altura <= 0:
        return jsonify({"erro": "Peso e altura devem ser maiores que zero"}), 400
    
    imc = peso / (altura ** 2)
    imc_arredondado = round(imc, 2)
    
    if imc < 18.5:
        classificacao = "🔵 Abaixo do peso"
        cor = "#38bdf8"
    elif imc < 25:
        classificacao = "🟢 Peso normal"
        cor = "#4ade80"
    elif imc < 30:
        classificacao = "🟡 Sobrepeso"
        cor = "#facc15"
    elif imc < 35:
        classificacao = "🟠 Obesidade grau 1"
        cor = "#fb923c"
    elif imc < 40:
        classificacao = "🔴 Obesidade grau 2"
        cor = "#f87171"
    else:
        classificacao = "⚫ Obesidade grau 3 (mórbida)"
        cor = "#a3a3a3"
    
    return jsonify({
        "imc": imc_arredondado,
        "classificacao": classificacao,
        "cor": cor
    })


def abrir_navegador():
    webbrowser.open_new_tab("http://127.0.0.1:5000")


if __name__ == "__main__":
    print("=" * 50)
    print("  Calculadora de IMC - Frontend + Backend")
    print("=" * 50)
    print("Backend rodando em: http://127.0.0.1:5000")
    print("Abrindo o frontend no navegador...")
    print("Pressione CTRL+C para parar o servidor.")
    print("=" * 50)
    
    threading.Timer(1.0, abrir_navegador).start()
    app.run(host="127.0.0.1", port=5000, debug=False)
