import { createRouter, createWebHistory } from 'vue-router';

const Home = () => import('@/pages/Home.vue');
const Shop = () => import('@/pages/Shop.vue');
const Community = () => import('@/pages/community/Community.vue');
const FloatPopular = () => import('@/pages/InfoPlaza/FloatPopular.vue');
const RentalInfo = () => import('@/pages/InfoPlaza/RentalInfo.vue');
const BoardCreate = () => import('@/pages/community/BoardCreate.vue');
const BoardView = () => import('@/pages/community/BoardView.vue');
const PopularIndustry = () => import('@/pages/InfoPlaza/PopularIndustry.vue');
const TotalTrendingBusinessItems = () => import('@/pages/InfoPlaza/TotalTrendingBusinessItems.vue');
const MylocationTrending = () => import('@/pages/InfoPlaza/MyLocatinTrending.vue');
const CloseRatio = () => import('@/pages/InfoPlaza/CloseRatio.vue');
const StoreInfo = () => import('@/pages/InfoPlaza/StoreInfo.vue');
const PersonalLoan = () => import('@/pages/Infoplaza/PersonalLoan.vue');
const LoanDetail = () => import('@/pages/InfoPlaza/LoanDetail.vue');
const EnterpriseLoan = () => import('@/pages/Infoplaza/EnterpriseLoan.vue');
const Education = () => import('@/pages/InfoPlaza/Education.vue');
const Video = () => import('@/pages/InfoPlaza/Video.vue');
const news = () => import('@/pages/InfoPlaza/news.vue');
const Report = () => import('@/pages/simul/Report.vue');
const MyStore = () => import('@/pages/asset/MyStore.vue');
const Mypage = () => import('@/pages/mypage/Report.vue');
const StoreReg = () => import('@/pages/asset/StoreReg.vue');
const InfoAgree = () => import('@/pages/asset/InfoAgree.vue');
const AssetSelect = () => import('@/pages/asset/AssetSelect.vue');
const AssetReg = () => import('@/pages/asset/AssetReg.vue');
const AssetFin = () => import('@/pages/asset/AssetFin.vue');
const Simul = () => import('@/pages/simul/Simul.vue');
const Register = () => import('@/pages/register/Register.vue');
const Login = () => import('@/pages/login/Login.vue');
const MypageUpdate = () => import('@/components/mypage/MypageUpdate.vue');
const MypageReport = () => import('@/components/mypage/MypageReport.vue');

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'Home', component: Home },
    { path: '/shop', name: 'Shop', component: Shop },
    { path: '/community', name: 'Community', component: Community },
    { path: '/community/create', name: 'BoardCreate', component: BoardCreate },
    { path: '/community/view', name: 'BoardView', component: BoardView },
    {
      path: '/infoPlaza/industry',
      name: 'Industry',
      component: PopularIndustry,
    },
    {
      path: '/infoPlaza/industry/totalTrendingBusinessItems',
      name: 'totalTrendingBusinessItems',
      component: TotalTrendingBusinessItems,
    },
    {
      path: '/infoPlaza/industry/mylocationTrending',
      name: 'mylocationTrending',
      component: MylocationTrending,
    },
    {
      path: '/infoPlaza/industry/closeRatio',
      name: 'closeRatio',
      component: CloseRatio,
    },
    {
      path: '/infoPlaza/personalLoan',
      name: 'ersonalLoan',
      component: PersonalLoan,
    },
    {
      path: '/infoPlaza/enterpriseLoan',
      name: 'enterpriseLoan',
      component: EnterpriseLoan,
    },
    {
      path: '/infoPlaza/personalLoan/loanDetail',
      name: 'loanDetail',
      component: LoanDetail,
    },

    { path: '/infoPlaza/storeInfo', name: 'storeInfo', component: StoreInfo },
    {
      path: '/infoPlaza/floatpopular',
      name: 'FloatPopular',
      component: FloatPopular,
    },
    { path: '/infoPlaza/rentalinfo', name: 'RentalInfo', component: RentalInfo },
    { path: '/infoPlaza/education', name: 'education', component: Education },
    {
      path: '/infoplaza/education/video/:vno',
      name: 'video',
      component: Video, // 비디오 상세보기 컴포넌트 연결
      props: true, // route param을 컴포넌트에 props로 전달
    },
    { path: '/infoPlaza/news', name: 'news', component: news },
    // { path: '/infoPlaza/education/video', name: 'video', component: Video },
    { path: '/simul/report', name: 'Report', component: Report },
    { path: '/asset', name: 'MyStore', component: MyStore },
    { path: '/asset/infoagree', name: 'InfoAgree', component: InfoAgree },
    { path: '/asset/assetselect', name: 'AssetSelect', component: AssetSelect },
    { path: '/asset/assetfin', name: 'AssetFin', component: AssetFin },
    { path: '/asset/assetreg', name: 'AssetReg', component: AssetReg },
    { path: '/mypage', name: 'Mypage', component: Mypage },
    { path: '/asset/storereg', name: 'StoreReg', component: StoreReg },
    { path: '/simul', name: 'Simul', component: Simul },
    { path: '/register', name: 'Register', component: Register },
    { path: '/login', name: 'Login', component: Login },
    { path: '/mypageupdate', name: 'MypageUpdate', component: MypageUpdate },
    { path: '/mypagereport', name: 'MypageReport', component: MypageReport },
    // { path: '/input', name: "Input", component: Input },
    // { path: '/input2', name: "Input2", component: Input2 },
    // { path: '/update', name: "Update", component: Update },
  ],
});

export default router;
