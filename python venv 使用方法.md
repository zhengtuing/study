

### python venv 使用方法





在 Python 3 中，你可以使用 `venv` 模块来创建和管理虚拟环境。以下是创建和设置 Python 3 虚拟环境的步骤：

1. 打开终端窗口。

2. 使用以下命令创建一个新的虚拟环境。你需要指定一个目标文件夹的路径，这是你的虚拟环境将会被创建的地方。例如，假设你想在当前目录下创建一个名为 "myenv" 的虚拟环境，你可以运行以下命令：

   + 在macOS 和 Linux中，运行以下命令：

     ```shell
     python3 -m venv myvenv
     ```
   
   + 在 windows中，运行以下命令：
   
     ```shell
     python -m venv myvenv
     ```

​		这将创建一个名为 "myenv" 的虚拟环境。



3. 激活虚拟环境。在不同的操作系统中，激活命令有所不同：
   - 在 macOS 和 Linux 中，运行以下命令：
     ```shell
     source myenv/bin/activate
     ```
   - 在 Windows 中，运行以下命令：
     ```shell
     myenv\Scripts\activate
     ```

   一旦虚拟环境被激活，你将在终端提示符前看到虚拟环境的名称，表示你正在使用虚拟环境。

4. 在激活的虚拟环境中，你可以安装和管理特定于该环境的 Python 包，而不会影响系统范围的 Python 安装。

5. 当你完成工作后，可以使用以下命令来退出虚拟环境：

   ```shell
   deactivate
   ```

   这将使虚拟环境停止激活，你将返回到系统范围的 Python 环境。

## django 项目迁移
    1. 安装python
       
        - `$ sudo apt install python3`
    2. 安装相同版本的包
        - 导出当前模块数据包的信息:
            - `$ pip3 freeze > package_list.txt`
        - 导入到另一台新主机
            - `$ pip3 install -r package_list.txt`
