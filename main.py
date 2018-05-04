import os
import time
import vk_api
from vk_api import VkUpload

def main():
    token = os.environ['USER_TOKEN']
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()

    upload = VkUpload(vk_session)
    while True:
        photo = upload.photo_wall(
            'gNoAu8mj8hE.jpg',
            group_id=166009300
        )

        media_id = 'photo{}_{}'.format(
            photo[0]['owner_id'], photo[0]['id']
        )

        vk.wall.post(owner_id=-166009300, friends_only=0, from_group=1,attachments=(photo, photo[0]['owner_id'], media_id), signed=0)
        time.sleep(60)

if __name__ == '__main__':
    main()