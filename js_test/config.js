import {astro} from 'iztro';

console.log("默认配置: ", astro.getConfig())
const config = {
    'mutagens': {'庚': ['太阳', '武曲', '天同', '天相']},
    'brightness': {'贪狼': ['旺', '旺', '旺', '旺', '旺', '旺', '旺', '旺', '旺', '旺', '旺', '旺']},
}

astro.config(config)
console.log("修改后配置: ", astro.getConfig())
