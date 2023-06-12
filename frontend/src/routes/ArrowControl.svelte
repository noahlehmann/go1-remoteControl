<script>
    import ArrowUp from "svelte-material-icons/ArrowUp.svelte";
    import ArrowDown from "svelte-material-icons/ArrowDown.svelte";
    import ArrowLeft from "svelte-material-icons/ArrowLeft.svelte";
    import ArrowRight from "svelte-material-icons/ArrowRight.svelte";
    import {writable} from "svelte/store";

    export let size = "50px";
    export let width = size;
    export let height = size;
    export let upColor = writable("black");
    export let downColor = writable("black");
    export let leftColor = writable("black");
    export let rightColor = writable("black");

    export function highlight(values){
        if (values.up !== undefined) upColor.set(values.up?"red":"black");
        if (values.down !== undefined) downColor.set(values.down?"red":"black");
        if (values.left !== undefined) leftColor.set(values.left?"red":"black");
        if (values.right !== undefined) rightColor.set(values.right?"red":"black");
    }
</script>

<section>
    <div class="vertical">
        <ArrowUp {width} {height} color={$upColor} class="arrow"/>
    </div>
    <div class="horizontal">
        <ArrowLeft {width} {height} color={$leftColor} class="arrow"/>
        <ArrowRight {width} {height} color={$rightColor} class="arrow"/>
    </div>
    <div class="vertical">
        <ArrowDown {width} {height} color={$downColor} class="arrow"/>
    </div>
</section>

<style>
    section {
        flex: 1;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 20px;
        min-width: 20vw;
        padding: 2em;
    }
    .vertical {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
    }
    .horizontal {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
        gap: 100px;
    }
    .arrow {
        padding: 1rem;
    }
</style>
