"""
框架入口：直接运行脚本（非 pytest）时使用。
等价于在终端执行：pytest tests/ -v
"""
import subprocess
import sys


def main():
    result = subprocess.run(
        [sys.executable, '-m', 'pytest', 'tests/', '-v', '--tb=short'],
        cwd='.',
    )
    sys.exit(result.returncode)


if __name__ == '__main__':
    main()
