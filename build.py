#!/usr/bin/env python3
import subprocess
import os
import sys
import shutil

# Limpar tudo antes de compilar
print("[CLEAN] Limpando cache e builds anteriores...")
gradle_cache = os.path.expanduser("~/.gradle")
build_dir = "app/build"

if os.path.exists(gradle_cache):
    try:
        shutil.rmtree(gradle_cache)
        print("[CLEAN] Cache gradle removido")
    except Exception as e:
        print(f"[WARN] Nao conseguiu remover cache: {e}")

if os.path.exists(build_dir):
    try:
        shutil.rmtree(build_dir)
        print("[CLEAN] Diretorio build removido")
    except Exception as e:
        print(f"[WARN] Nao conseguiu remover build: {e}")

# Limpar JAVA_HOME problemático
for key in list(os.environ.keys()):
    if 'JAVA' in key.upper():
        del os.environ[key]

# Configurar JAVA correto
java_home = r"C:\Program Files\Java\jdk-17"
os.environ['JAVA_HOME'] = java_home
os.environ['GRADLE_OPTS'] = "-Xmx1024m -XX:+UseParallelGC"
os.environ['PATH'] = f"{java_home}\\bin;" + os.environ.get('PATH', '')

os.chdir(r"c:\App_Controle_Financeiro")

# Executar gradle com otimizações
cmd = [
    r".\gradlew.bat", 
    "clean",
    "assembleDebug",
    "--parallel",
    "--max-workers=4",
    "-x", "lint",
    "-x", "testDebugUnitTest",
    "--no-daemon"
]

print("[BUILD] Compilando APK...")
print(f"[BUILD] Comando: {' '.join(cmd)}\n")

result = subprocess.run(cmd, shell=True)

# Verificar se APK foi gerado
import glob
apks = glob.glob(r"app\build\outputs\apk\debug\*.apk")
if apks:
    print(f"\n[OK] APK PRONTO: {apks[0]}")
    import os.path
    size_mb = round(os.path.getsize(apks[0]) / (1024*1024), 2)
    print(f"[SIZE] Tamanho: {size_mb} MB")
    print("\n[INSTALL] Para instalar, execute: .\\instalar.ps1")
else:
    print("\n[ERROR] Erro: APK nao foi gerado")
    sys.exit(1)


