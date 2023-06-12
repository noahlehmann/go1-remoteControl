<script>
    import './styles.css';
    import Header from "./Header.svelte";
    import StatusFooter from "./StatusFooter.svelte";
</script>

<div class="app">
    <header>
        <Header/>
    </header>

    <main>
        <slot/>
    </main>

    <footer>
        <StatusFooter/>
    </footer>

</div>

<style>
    .app {
        display: flex;
        flex-direction: column;
        min-height: 100vh;
    }

    main {
        flex: 1;
        display: flex;
        flex-direction: column;
        padding: 1rem;
        width: 100%;
        margin: 0 auto;
        box-sizing: border-box;
    }
</style>
