let currentMode = 'vulnerable';

function setMode(mode) {
    currentMode = mode;
    document.getElementById('btn-vuln').classList.toggle('active', mode === 'vulnerable');
    document.getElementById('btn-sec').classList.toggle('active', mode === 'secure');
    addLog(`[SYSTEM] Switched endpoint to: /${mode.toUpperCase()}`);
}

function fillPayload() {
    // Fills the input with a classic SQL Injection payload
    document.getElementById('username').value = "' OR '1'='1";
    document.getElementById('password').value = "' OR '1'='1";
}

document.getElementById('loginForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    addLog(`[USER] Sending credentials...`);

    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);

    try {
        const response = await fetch(`/${currentMode}`, { method: 'POST', body: formData });
        const data = await response.json();
        
        addLog(`[DB] Executing Query:`, 'log-prefix');
        addLog(`${data.query}`, 'log-query');

        if (data.success) {
            addLog(`[SUCCESS] ACCESS GRANTED. User: ${data.user}`, 'log-success');
        } else {
            addLog(`[FAIL] ACCESS DENIED.`, 'log-fail');
            if(data.message.includes("Syntax Error")) {
                addLog(`[ERROR] DB CRASH: ${data.message}`, 'log-fail');
            }
        }

    } catch (error) {
        addLog(`[ERROR] Network Failure`, 'log-fail');
    }
});

function addLog(text, className = '') {
    const logContainer = document.getElementById('terminal-logs');
    const entry = document.createElement('div');
    entry.className = `log-entry ${className}`;
    entry.innerText = text.startsWith('>') ? text : `> ${text}`;
    logContainer.appendChild(entry);
    logContainer.scrollTop = logContainer.scrollHeight;
}