# Django跨域设置

在Django中设置跨域请求通常涉及到安装和配置`django-cors-headers`这个库。下面是配置跨域请求的基本步骤：

1. **安装django-cors-headers**：首先，你需要安装这个库。你可以使用pip来安装：

   ```bash
   pip install django-cors-headers
   ```

2. **添加CORS中间件**：接着，在你的Django项目的`settings.py`文件中，将CORS中间件添加到`MIDDLEWARE`配置中。确保将它添加在`CommonMiddleware`之前。

   ```python
   MIDDLEWARE = [
       # ...
       'django.middleware.common.CommonMiddleware',
       'corsheaders.middleware.CorsMiddleware',
       # ...
   ]
   ```

3. **配置CORS**：在`settings.py`中，你可以设置CORS的一些基本规则。例如，允许所有来源的跨域请求：

   ```python
   CORS_ALLOW_ALL_ORIGINS = True
   ```

   或者，你可以指定允许哪些域进行跨域请求：

   ```python
   CORS_ALLOWED_ORIGINS = [
       "https://example.com",
       "https://sub.example.com",
       "http://localhost:8080",
       "http://127.0.0.1:9000",
   ]
   ```

4. **配置额外的CORS设置（可选）**：根据你的需求，你可能还需要配置额外的CORS相关设置，如允许特定的头部、HTTP方法等。这些设置可以在`settings.py`中配置。例如，允许所有头部和HTTP方法：

   ```python
   CORS_ALLOW_ALL_HEADERS = True
   CORS_ALLOW_METHODS = [
       "DELETE",
       "GET",
       "OPTIONS",
       "PATCH",
       "POST",
       "PUT",
   ]
   ```

5. **重新启动Django服务器**：配置完成后，重新启动你的Django服务器，以使更改生效。

请注意，允许所有来源的跨域请求可能会带来安全风险，因此在生产环境中，你应该尽可能具体地指定允许的来源。