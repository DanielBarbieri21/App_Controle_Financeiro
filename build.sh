#!/usr/bin/env bash
set -e

export JAVA_HOME="/c/Program Files/Java/jdk-17"
export PATH="$JAVA_HOME/bin:$PATH"

cd /c/App_Controle_Financeiro

echo "🔨 Compilando APK..."
./gradlew.bat assembleDebug --parallel --max-workers=4 -x lint

if [ -f "app/build/outputs/apk/debug/app-debug.apk" ]; then
    echo "✅ APK gerado com sucesso!"
    ls -lh app/build/outputs/apk/debug/app-debug.apk
else
    echo "❌ Erro: APK não foi gerado"
    exit 1
fi
