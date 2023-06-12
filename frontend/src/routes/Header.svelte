<script>
    import Menu from "svelte-material-icons/Menu.svelte";
    import ColorHelper from "svelte-material-icons/ColorHelper.svelte"
</script>

<section>
    <Menu/>
    <ColorHelper/>
</section>


<style>
    section {
        flex: 1;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
    }
</style>