<template>
<div class="list-group list-group-flush gap-2">
    <!-- 유동인구 항목 -->
    <div class="list-group-item gap-3 text-center p-3 bg-body-secondary-hover">
    <div class="icon flex-none">
        <img 
        :src="currentRoute == '/infoPlaza/floatpopular' || currentRoute == '/'
                ? popularImg 
                : nopopularImg" 
        class="w-rem-8 h-rem-8" 
        alt="유동인구">
    </div>
    <div class="align-items-center flex-fill">
        <div>
            <a 
            v-if="currentRoute !== '/infoPlaza/floatpopular' && currentRoute !== '/'" 
            href="/infoPlaza/floatpopular" 
            class="stretched-link text-heading text-sm fw-bold">
            유동인구
            </a>
            <span 
            v-else 
            class="text-heading text-sm fw-bold text-muted" 
            style="pointer-events: none;"> <!-- 비활성화된 상태로 보이도록 스타일 추가 -->
            유동인구
            </span>
        </div>
    </div>
    </div>

    <!-- 임대정보 항목 -->
    <div class="list-group-item gap-3 p-3 text-center bg-body-secondary-hover">
    <div class="icon flex-none">
        <img 
        :src="currentRoute === '/infoPlaza/rentalinfo' 
                ? addBusinessImg
                : noAddBusinessImg" 
        class="w-rem-8 h-rem-8" 
        alt="임대정보">
        
    </div>
    <div class="align-items-center flex-fill">
        <div>
            <a 
            v-if="currentRoute !== '/infoPlaza/rentalinfo'" 
            href="/infoPlaza/rentalinfo" 
            class="stretched-link text-heading text-sm fw-bold">
            임대정보
            </a>
            <span 
            v-else 
            class="text-heading text-sm fw-bold text-muted" 
            style="pointer-events: none;"> <!-- 비활성화된 상태로 보이도록 스타일 추가 -->
            임대정보
            </span>
        </div>
    </div>
    </div>
</div>
</template>

<script setup>
import { useRoute } from 'vue-router';

// 현재 경로를 가져옴
const route = useRoute();
const currentRoute = route.path;

// 이미지 경로 설정 (import로 경로를 지정)
import popularImg from '@/assets/img/infoplaza/popular.png';
import addBusinessImg from '@/assets/img/infoplaza/add_business.png';
import noAddBusinessImg from '@/assets/img/infoplaza/no_add_business.png';
import nopopularImg from '@/assets/img/infoplaza/no_popular.png';
</script>

<style>
/* 스타일 필요시 추가 */
</style>
