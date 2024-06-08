<template>
    <q-page padding>
        <div class="flex justify-center">

            <div class="flex flex-auto">
                <!-- <Flicking style="width: 500px; overflow-x:auto;" :options="{ circular: true }" :plugins="plugins">
                <q-card class="my-card panel" v-for="v in 10" :key="v">
                    <q-card-section>
                        {{ lorem }}
                    </q-card-section>
                </q-card>
            </Flicking> -->
                <Flicking style="width: 500px; overflow-x:auto;" :options="{ circular: true }" :plugins="plugins">
                    <q-card>
                        <q-card-section> 1</q-card-section>
                    </q-card>
                    <q-card>
                        <q-card-section> 1</q-card-section>
                    </q-card>
                    <q-card>
                        <q-card-section> 1</q-card-section>
                    </q-card>
                </Flicking>
            </div>

        </div>

        <h1>asdasd</h1>
    </q-page>
</template>

<script setup>

import Flicking from '@egjs/vue3-flicking';
import { Perspective } from '@egjs/flicking-plugins';
import '@egjs/flicking-plugins/dist/flicking-plugins.css';

const plugins = [new Perspective({ fade: true })];

// const lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nec purus ut sem fermentum tincidunt. Nullam nec purus ut sem fermentum tincidunt.';
</script>

<style scoped>
.flicking {
    width: 500px;
    height: 130px;
    margin: 0px auto;
    background: #eee;
    background: rgba(55, 55, 55 0.1);
    border-radius: 5px;
}

.flicking .panel0,
.flicking .panel1,
.flicking .panel2,
.flicking .panel3,
.flicking .panel4,
.flicking .infinite {
    position: relative;
    display: block;
    border-radius: 5px;
    width: 200px;
    margin-top: 5px;
    background: #f55;
    height: 120px;
    text-align: center;
    line-height: 120px;
}

.flicking .panel0 {
    background: #F47071;
}

.flicking .panel1 {
    background: #F69462;
}

.flicking .panel2 {
    background: #EDE484;
}

.flicking .panel3 {
    background: #90F290;
}

.flicking .panel4 {
    background: #78CAFF;
}

/*
  Atom One Dark by Daniel Gamage
  Original One Dark Syntax theme from https://github.com/atom/one-dark-syntax

  base:    #282c34
  mono-1:  #abb2bf
  mono-2:  #818896
  mono-3:  #5c6370
  hue-1:   #56b6c2
  hue-2:   #61aeee
  hue-3:   #c678dd
  hue-4:   #98c379
  hue-5:   #e06c75
  hue-5-2: #be5046
  hue-6:   #d19a66
  hue-6-2: #e6c07b
  */
.hljs {
    display: block;
    overflow-x: auto;
    padding: 0.5em;
    color: #abb2bf;
    background: #282c34;
}

.hljs-comment,
.hljs-quote {
    color: #5c6370;
    font-style: italic;
}

.hljs-doctag,
.hljs-keyword,
.hljs-formula {
    color: #c678dd;
}

.hljs-section,
.hljs-name,
.hljs-selector-tag,
.hljs-deletion,
.hljs-subst {
    color: #e06c75;
}

.hljs-literal {
    color: #56b6c2;
}

.hljs-string,
.hljs-regexp,
.hljs-addition,
.hljs-attribute,
.hljs-meta-string {
    color: #98c379;
}

.hljs-built_in,
.hljs-class .hljs-title {
    color: #e6c07b;
}

.hljs-attr,
.hljs-variable,
.hljs-template-variable,
.hljs-type,
.hljs-selector-class,
.hljs-selector-attr,
.hljs-selector-pseudo,
.hljs-number {
    color: #d19a66;
}

.hljs-symbol,
.hljs-bullet,
.hljs-link,
.hljs-meta,
.hljs-selector-id,
.hljs-title {
    color: #61aeee;
}

.hljs-emphasis {
    font-style: italic;
}

.hljs-strong {
    font-weight: bold;
}

.hljs-link {
    text-decoration: underline;
}

.plugins h1 {
    line-height: 1;
}

.plugins h1 a {
    font-size: 20px;
    vertical-align: bottom;
    margin-left: 10px;
    /* color: #55e; */
}

.plugins .flicking {
    width: 500px;
    height: 200px;
    margin: 0px auto;
    background: #eee;
    background: rgba(55, 55, 55 0.1);
    border-radius: 5px;
}

.plugins .flicking .panel {
    position: relative;
    display: block;
    border-radius: 5px;
    width: 400px;
    margin-top: 5px;
    background: #f55;
    height: 200px;
    text-align: center;
    line-height: 200px;
    overflow: hidden;
}

.plugins .panel:after {
    content: "";
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    background: rgba(0, 0, 0, 0.1);
}

.plugins .panel img {
    top: -100%;
    bottom: -100%;
    margin: auto;
    position: absolute;
    left: 50%;
    transform: translate(-50%);
}


a {
    margin: 10px;
}

.component-fade-enter-active,
.component-fade-leave-active {
    transition: opacity .3s ease;
}

.component-fade-enter,
.component-fade-leave-to

/* .component-fade-leave-active below version 2.1.8 */
    {
    opacity: 0;
}
</style>