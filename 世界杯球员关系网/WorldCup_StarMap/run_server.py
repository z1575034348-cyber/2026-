"""
比利时队世界杯关系星图 - 本地预览服务器
==========================================
极简 Python HTTP 服务，解决浏览器直接打开 HTML 时的 CORS 问题。
自动检测可用端口，启动后在浏览器访问即可预览。
"""

import http.server
import socketserver
import os
import sys
import socket
from pathlib import Path

# 切换到脚本所在目录
os.chdir(Path(__file__).parent.resolve())

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({
    '.json': 'application/json',
    '.html': 'text/html',
    '.js': 'application/javascript',
    '.css': 'text/css',
})


class NoCacheHandler(Handler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()


def get_server(port):
    """尝试在指定端口创建服务器，失败则返回 None"""
    class ReusableTCPServer(socketserver.TCPServer):
        allow_reuse_address = True

    try:
        server = ReusableTCPServer(("", port), NoCacheHandler)
        return server
    except OSError:
        return None


if __name__ == '__main__':
    # 直接尝试绑定端口，而不是用 connect_ex (后者在 Windows 上可能卡死)
    httpd = None
    for PORT in range(8080, 8095):
        httpd = get_server(PORT)
        if httpd:
            break

    if httpd is None:
        print("错误: 8080-8094 端口全部被占用，请先关闭其他程序后重试。")
        sys.exit(1)

    print('=' * 60)
    print('  比利时队 · 世界杯关系星图')
    print('  World Cup Drama Star Map — Belgium')
    print('=' * 60)
    print()
    print(f'  本地服务已启动: http://localhost:{PORT}')
    print(f'  服务目录: {os.getcwd()}')
    print()
    print('  请在浏览器中打开上述地址查看星图。')
    print('  按 Ctrl+C 停止服务。')
    print('=' * 60)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\n\n服务已停止。再见!')
        sys.exit(0)
