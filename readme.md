Nextcloud with video thumbnail generation

## Run

1. Run

```sh
./manage.py run minio dev
# Another tab
./manage.py run nextcloud dev
```

2. Add secret key in http://localhost:3001 if running locally
3. Install preview generator app from admin console
4. Add to `./nextcloud/config/config.php`

```php
'ffmpeg' => '/usr/bin/ffmpeg',
'enable_previews' => true,
'enabledPreviewProviders' =>
array (
    0 => 'OC\\Preview\\PNG',
    1 => 'OC\\Preview\\JPEG',
    2 => 'OC\\Preview\\GIF',
    3 => 'OC\\Preview\\BMP',
    4 => 'OC\\Preview\\XBitmap',
    5 => 'OC\\Preview\\Movie',
    6 => 'OC\\Preview\\PDF',
    7 => 'OC\\Preview\\MP3',
    8 => 'OC\\Preview\\TXT',
    9 => 'OC\\Preview\\MarkDown',
    10 => 'OC\\Preview\\MP4',
),
```

5. Generate first preview on the go (replace `nextcloud-docker-s3-deploy-nextcloud-1` with your tag name)
```sh
docker exec -u www-data -it nextcloud-docker-s3-deploy-nextcloud-1 ./occ preview:generate-all -vvv
```