import { createRouter, createWebHistory } from 'vue-router';

const Home = () => import('@/pages/Home.vue');
const Shop = () => import('@/pages/Shop.vue');
const Community = () => import('@/pages/community/Community.vue');
const FloatPopular = () => import('@/pages/InfoPlaza/FloatPopular.vue');
const RentalInfo = () => import('@/pages/InfoPlaza/RentalInfo.vue');
const BoardCreate = () => import('@/pages/community/BoardCreate.vue');
const BoardView = () => import('@/pages/community/BoardView.vue');
const PopularIndustry = () => import('@/pages/InfoPlaza/PopularIndustry.vue');
const TotalTrendingBusinessItems = () =>
  import('@/pages/InfoPlaza/TotalTrendingBusinessItems.vue');
const MylocationTrending = () =>
  import('@/pages/InfoPlaza/MyLocatinTrending.vue');
const CloseRatio = () => import('@/pages/InfoPlaza/CloseRatio.vue');
const StoreInfo = () => import('@/pages/InfoPlaza/StoreInfo.vue');
const GovernmentFund = () => import('@/pages/Infoplaza/GovernmentFund.vue');
const GovernmentFundDetail = () =>
  import('@/pages/InfoPlaza/GovernmentFundDetail.vue');
const PersonalCreditLoan = () =>
  import('@/pages/Infoplaza/PersonalCreditLoan.vue');
const PersonalCreditLoanDetail = () =>
  import('@/pages/Infoplaza/PersonalCreditLoanDetail.vue');
const EnterpriseLoan = () => import('@/pages/Infoplaza/EnterpriseLoan.vue');
const KBLoan = () => import('@/pages/Infoplaza/KBLoan.vue');
const KBLoanDetail = () => import('@/pages/Infoplaza/KBLoanDetail.vue');
const JeonseLoan = () => import('@/pages/Infoplaza/JeonseLoan.vue');
const JeonseLoanDetail = () => import('@/pages/Infoplaza/JeonseLoanDetail.vue');
const MortgageLoan = () => import('@/pages/Infoplaza/MortgageLoan.vue');
const MortgageLoanDetail = () =>
  import('@/pages/Infoplaza/MortgageLoanDetail.vue');
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
//    { path: '/community', name: 'Community', component: Community },
    {
      path: '/community/:category',
      name: 'Community',
      component: Community,
    },
    //{ path: '/community/create', name: 'BoardCreate', component: BoardCreate },
    //{ path: '/community/view', name: 'BoardView', component: BoardView },
    {
      path: '/community/:category/view/:postId',
      name: 'BoardView',
      component: BoardView,
    },
    {
      path: '/community/:category/create',
      name: 'BoardCreate',
      component: BoardCreate,
    },
    {
      path: '/community/:category/edit/:postId',
      name: 'BoardCreate',
      component: BoardCreate, // 같은 컴포넌트를 사용
    },
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
      path: '/infoPlaza/governmentFund',
      name: 'governmentFund',
      component: GovernmentFund,
    },
    {
      path: '/infoPlaza/personalCreditLoan',
      name: 'personalCreditLoan',
      component: PersonalCreditLoan,
    },
    {
      path: '/infoPlaza/jeonseLoan',
      name: 'jeonseLoan',
      component: JeonseLoan,
    },
    {
      path: '/infoPlaza/mortgageLoan',
      name: 'mortgageLoan',
      component: MortgageLoan,
    },
    {
      path: '/infoPlaza/KBLoan',
      name: 'KBLoan',
      component: KBLoan,
    },
    {
      path: '/infoPlaza/enterpriseLoan',
      name: 'enterpriseLoan',
      component: EnterpriseLoan,
    },
    {
      path: '/infoPlaza/governmentFund/governmentFundDetail/:productName',
      name: 'governmentFundDetail',
      component: GovernmentFundDetail,
    },
    {
      path: '/infoPlaza/personalCreditLoan/personalCreditLoanDetail/:id',
      name: 'personalCreditLoanDetail',
      component: PersonalCreditLoanDetail,
    },
    {
      path: '/infoPlaza/jeonseLoan/jeonseLoanDetail/:id',
      name: 'jeonseLoanDetail',
      component: JeonseLoanDetail,
    },
    {
      path: '/infoPlaza/mortgageLoan/mortgageLoanDetail/:id',
      name: 'mortgageLoanDetail',
      component: MortgageLoanDetail,
    },
    {
      path: '/infoPlaza/KBLoan/KBLoanDetail/:productName',
      name: 'KBLoanDetail',
      component: KBLoanDetail,
    },

    { path: '/infoPlaza/storeInfo', name: 'storeInfo', component: StoreInfo },
    {
      path: '/infoPlaza/floatpopular',
      name: 'FloatPopular',
      component: FloatPopular,
    },
    {
      path: '/infoPlaza/rentalinfo',
      name: 'RentalInfo',
      component: RentalInfo,
    },
    { path: '/infoPlaza/education', name: 'education', component: Education },
    { path: '/infoPlaza/news', name: 'news', component: news },
    { path: '/infoPlaza/education/video', name: 'video', component: Video },
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
