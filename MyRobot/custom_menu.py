from werobot import WeRoBot
import mcdb.config as CONFIG


robot = WeRoBot(token="tiandaotiyu")
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 8000
robot.config["APP_ID"] = CONFIG.app_id
robot.config["APP_SECRET"] = CONFIG.app_secret

client = robot.client

client.create_menu({
    "button":[
        {
            "type": "view",
            "name": "进入主页",
            "url": CONFIG.r_oauth
        },
        {
            "type": "view",
            "name": "老师登录",
            "url": CONFIG.prelogin_teacher
        }
    ]
})

